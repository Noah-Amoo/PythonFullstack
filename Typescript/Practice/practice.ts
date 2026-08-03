// TypeScript Practice Sheet
// Basic -> Advanced concepts, including generics

// 1) Basic types
let username: string = "noah";
let age: number = 25;
let isLoggedIn: boolean = true;
let favoriteScore: number | string = 99;

console.log("Basic types:", username, age, isLoggedIn, favoriteScore);
// Try this: change favoriteScore to a string like "A+" and rerun the file.

// 2) Arrays and tuples
let skills: string[] = ["HTML", "CSS", "TypeScript"];
let userTuple: [string, number, boolean] = ["Alice", 30, true];

console.log("Arrays and tuples:", skills, userTuple);
// Try this: add one more skill, then try swapping tuple item order and observe the type error.

// 3) Object types and type aliases
type User = {
  id: number;
  name: string;
  email?: string;
};

const user1: User = {
  id: 1,
  name: "Ava",
};

console.log("Object type:", user1);
// Try this: add email to user1, then remove name to see required property checking.

// 4) Union and intersection types
type ID = string | number;

type Employee = {
  employeeId: ID;
  department: string;
};

type ContactInfo = {
  phone: string;
  city: string;
};

type EmployeeProfile = Employee & ContactInfo;

const employee: EmployeeProfile = {
  employeeId: 101,
  department: "Engineering",
  phone: "+1-555-1000",
  city: "New York",
};

console.log("Intersection type:", employee);
// Try this: change employeeId to a string and keep the rest the same.

// 5) Functions with typed parameters and return values
function addNumbers(a: number, b: number): number {
  return a + b;
}

function greet(name: string, greeting = "Hello"): string {
  return `${greeting}, ${name}!`;
}

console.log("Functions:", addNumbers(10, 20), greet("TypeScript"));
// Try this: make greet accept a different default greeting.

// 6) Optional and default parameters
function buildProfile(name: string, role?: string): string {
  return role ? `${name} works as ${role}` : `${name} has no role assigned`;
}

console.log(
  "Optional param:",
  buildProfile("Sam"),
  buildProfile("Sam", "Developer"),
);
// Try this: pass a role like "Designer" and then omit it entirely.

// 7) Literal types and narrowing
type Status = "idle" | "loading" | "success" | "error";

function renderStatus(status: Status): string {
  if (status === "loading") {
    return "Loading...";
  }

  if (status === "error") {
    return "Something went wrong";
  }

  return `Status: ${status}`;
}

console.log("Literal union:", renderStatus("success"));
// Try this: call renderStatus with "loading" and "error".

// 8) Interfaces
interface Product {
  productId: number;
  title: string;
  price: number;
}

const product: Product = {
  productId: 2001,
  title: "Mechanical Keyboard",
  price: 79.99,
};

console.log("Interface:", product);
// Try this: add a new property to Product and update product accordingly.

// 9) Classes and access modifiers
class BankAccount {
  private balance: number;

  constructor(
    public accountHolder: string,
    initialBalance: number,
  ) {
    this.balance = initialBalance;
  }

  deposit(amount: number): void {
    this.balance += amount;
  }

  withdraw(amount: number): boolean {
    if (amount > this.balance) {
      return false;
    }

    this.balance -= amount;
    return true;
  }

  getBalance(): number {
    return this.balance;
  }
}

const account = new BankAccount("Maya", 500);
account.deposit(250);
account.withdraw(100);

console.log("Class:", account.accountHolder, account.getBalance());
// Try this: call withdraw with an amount greater than the balance and inspect the return value.

// 10) Enums
enum OrderStatus {
  Pending = "PENDING",
  Shipped = "SHIPPED",
  Delivered = "DELIVERED",
}

const currentOrderStatus: OrderStatus = OrderStatus.Shipped;
console.log("Enum:", currentOrderStatus);
// Try this: switch the status to Pending or Delivered.

// 11) Type narrowing with unknown
function parseValue(value: unknown): string {
  if (typeof value === "string") {
    return value.toUpperCase();
  }

  if (typeof value === "number") {
    return value.toFixed(2);
  }

  return "Unsupported value";
}

console.log("Narrowing:", parseValue("hello"), parseValue(42));
// Try this: pass a boolean or an object and compare the result.

// 12) Type assertion
const inputElement = { value: "Search text" } as { value: string };
console.log("Type assertion:", inputElement.value);
// Try this: change value to another string and remove the assertion shape.

// 13) Function overload example
function formatValue(value: string): string;
function formatValue(value: number): string;
function formatValue(value: string | number): string {
  return typeof value === "number" ? value.toFixed(1) : value.trim();
}

console.log("Overload:", formatValue("  hello  "), formatValue(12.345));
// Try this: call formatValue with a plain string and with a number that has more decimals.

// 14) Generic function
function identity<T>(value: T): T {
  return value;
}

console.log(
  "Generic function:",
  identity<string>("generic text"),
  identity<number>(123),
);
// Try this: remove the explicit type arguments and let TypeScript infer them.

// 15) Generic array helper
function getFirstItem<T>(items: T[]): T | undefined {
  return items[0];
}

console.log(
  "Generic array helper:",
  getFirstItem([10, 20, 30]),
  getFirstItem(["a", "b"]),
);
// Try this: pass an array of booleans or objects.

// 16) Generic interface
interface ApiResponse<T> {
  data: T;
  success: boolean;
  error?: string;
}

const userResponse: ApiResponse<User> = {
  data: user1,
  success: true,
};

console.log("Generic interface:", userResponse);
// Try this: change ApiResponse to hold Product instead of User.

// 17) Generic class
class StorageBox<T> {
  private items: T[] = [];

  add(item: T): void {
    this.items.push(item);
  }

  getAll(): T[] {
    return this.items;
  }
}

const numberBox = new StorageBox<number>();
numberBox.add(1);
numberBox.add(2);
console.log("Generic class:", numberBox.getAll());
// Try this: create another StorageBox for strings.

// 18) Generic constraint
function logLength<T extends { length: number }>(item: T): number {
  return item.length;
}

console.log(
  "Generic constraint:",
  logLength("typescript"),
  logLength([1, 2, 3]),
);
// Try this: pass an object with a length property.

// 19) keyof with generics
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

console.log("keyof generic:", getProperty(user1, "name"));
// Try this: use "id" or "email" as the key.

// 20) Mapped type example
type ReadOnlyUser = {
  readonly [K in keyof User]: User[K];
};

const readonlyUser: ReadOnlyUser = {
  id: 2,
  name: "Liam",
  email: "liam@example.com",
};

console.log("Mapped type:", readonlyUser);
// Try this: try changing a property on readonlyUser and observe the error.

// 21) Conditional type example
type IsString<T> = T extends string ? "yes" : "no";

type CheckOne = IsString<string>;
type CheckTwo = IsString<number>;

const checkOne: CheckOne = "yes";
const checkTwo: CheckTwo = "no";

console.log("Conditional type:", checkOne, checkTwo);
// Try this: create a new IsString<Date> type and see what it resolves to.

// 22) Your turn
// Exercises to try without looking up the answer immediately:
// - Create a typed function that filters only even numbers from an array.
// - Create an interface for a Todo item with id, title, and completed.
// - Build a generic function that swaps the order of a tuple.
// - Create a class that stores strings and returns the longest string.
// - Add a function that accepts unknown and safely narrows to a string array.
