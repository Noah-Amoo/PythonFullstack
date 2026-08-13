from fastapi import FastAPI, Form
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from pydantic import BaseModel

# service.name is how this app will be labeled in the Jaeger UI
resource = Resource.create({"service.name": "fastapi-otel-demo"})
tracer_provider = TracerProvider(resource=resource)
tracer_provider.add_span_processor(
	BatchSpanProcessor(OTLPSpanExporter(endpoint="localhost:4317", insecure=True))
)
trace.set_tracer_provider(tracer_provider)
tracer = trace.get_tracer(__name__)

app = FastAPI()
FastAPIInstrumentor.instrument_app(app)


class Item(BaseModel):
	name: str
	description: str | None = None
	price: float


items_db: list[Item] = []


@app.get("/")
def read_root() -> dict[str, str]:
	return {"message": "Home"}


@app.get("/items", response_model=list[Item])
def list_items() -> list[Item]:
	return items_db


def validate_item(item: Item) -> None:
	# child span nested under create_item_json's span
	with tracer.start_as_current_span("validate_item") as span:
		span.set_attribute("item.price", item.price)
		if item.price < 0:
			raise ValueError("price must be non-negative")


@app.post("/items/json", response_model=Item)
def create_item_json(item: Item) -> Item:
	# manual span nested under the auto-instrumented request span
	with tracer.start_as_current_span("create_item_json") as span:
		span.set_attribute("item.name", item.name)
		validate_item(item)
		items_db.append(item)
		return item


@app.post("/items/form", response_model=Item)
def create_item_form(
	name: str = Form(...),
	description: str | None = Form(None),
	price: float = Form(...),
) -> Item:
	item = Item(name=name, description=description, price=price)
	items_db.append(item)
	return item
