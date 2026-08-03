import ListGroup from "./components/ListGroup";
// import Alert from "./components/Alert";

const cities = ["UK", "Cambridge", "Luton"];

const onSelect = (city: string) => console.log(city);


export default function App() {
  return (
    // <div className="alert alert-primary">
    //   <Alert>Hello Noah. Welcome here!</Alert>
    // </div>
    <ListGroup items={cities} heading="Cities" onSelectItem={onSelect} />
  );
}
