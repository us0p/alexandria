# Clean Code
A guide for producing readable, reusable and refactorable software.
These are guidelines and nothing more.

## Guidelines list
- Variables
    - Use meaningful pronounceable variable names.
    - Use the same vocabulary for the same type of variable.
    - Use searchable names.
    - Avoid magic numbers.
    - Use explanatory variables
    - Avoid mental mapping, explicit is better than implicit.
    - Don't add uneeded context, if your class/object name tells something, 
      don't repeat that in your variable name.
- Functions
    - Use default parameters instead of short circuiting or conditionals.
    - Your functions should have at most 2 parameters, if strictly 
      necessary 3.
    - Functions should do one thing
    - Function names should say what they do
    - Functions should only be one level of abstraction.
    - Bad abstractions can be worse than duplicate code.
    - Don't use flags as functions parameters, flags tell your user that 
      this function does more than one thing.
    - Avoid Side Effects.
    - Favor functional programming over imperative programming.
    - Encapsulate conditional in functions.
    - Avoid negative conditionals.
- Classes
    - Avoid conditionals. You can use polymorphism to achieve the same 
      behaviour as an if statement in many cases.
    - Avoid type checking between classes, instead consider a more 
      consistent API.
    - Use getters and setters. When you want to do more beyond getting an 
      object property, you don't have to look up and change every accessor 
      in your codebase.
    - Make objects have private members.
    - Use method chaining, it allow your code to be expressive and less 
      verbose by applying imperative programming.
    - Prefer composition over inheritance.
- Tests
    - Single concept per test.
- General
    - Remove dead code, it'll be safe in your version history if you still 
      need it.
    - Function callers and callees should be close. If a function calls 
      another, keep those functions vertically close in the source file.
    - Only comment things that have business logic complexity.

## Variables
Use meaningful and pronounceable variable names.
```javascript
// bad:
const yyyymmdstr = moment().format("YYYY/MM/DD");

//good:
const currentDate = moment().format("YYYY/MM/DD");
```

Use the same vocabulary for the same type of variable.
```javascript
//bad:
getUserInfo();
getClientData();
getCustomerRecord();

//good:
getUser();
```

Use searchable names
```javascript
// bad:
// What the heck is 86400000 for?
setTimeout(blastOff, 86400000);

// good:
// Declare them as capitalized named constants.
const MILLISECONDS_PER_DAY = 60 * 60 * 24 * 1000; //86400000;

setTimeout(blastOff, MILLISECONDS_PER_DAY);
```

Use explanatory variables
```javascript
//bad:
const address = "One Infinite Loop, Cupertino 95014";
const cityZipCodeRegex = /^[^,\\]+[,\\\s]+(.+?)\s*(\d{5})?$/;
saveCityZipCode(
  address.match(cityZipCodeRegex)[1],
  address.match(cityZipCodeRegex)[2]
);

//good:
const address = "One Infinite Loop, Cupertino 95014";
const cityZipCodeRegex = /^[^,\\]+[,\\\s]+(.+?)\s*(\d{5})?$/;
const [_, city, zipCode] = address.match(cityZipCodeRegex) || [];
saveCityZipCode(city, zipCode);
```

Avoid mental mapping, explicit is better than implicit:
```javascript
//bad:
const locations = ["Austin", "New York", "San Francisco"];
locations.forEach(l => {
  dispatch(l);
});

//good:
const locations = ["Austin", "New York", "San Francisco"];
locations.forEach(location => {
  dispatch(location);
});
```

Don't add uneeded context, if your class/object name tells something, 
don't repeat that in your variable name:
```javascript
//bad:
const Car = {
  carMake: "Honda",
  carModel: "Accord",
  carColor: "Blue"
};

function paintCar(car, color) {
  car.carColor = color;
}

//good:
const Car = {
  make: "Honda",
  model: "Accord",
  color: "Blue"
};

function paintCar(car, color) {
  car.color = color;
}
```

Use default parameters instead of short circuiting or conditionals.
Default parameters are often cleaner than short circuiting.
```javascript
//bad:
function createMicrobrewery(name) {
  const breweryName = name || "Hipster Brew Co.";
  // ...
}

//good:
function createMicrobrewery(name = "Hipster Brew Co.") {
  // ...
}
```

## Functions
Your functions should have at most 2 parameters, if strictly necessary 3.
Having more than three leads to a combinatorial explosion where you have to
test tons of different cases with each separate argument.
Usually, if you have more than two arguments then your function is trying 
to do too much. In cases where it's not, most of the time a higher-level 
object will suffice as an argument.
```javascript
// bad:
function createMenu(title, body, buttonText, cancellable) {
  // ...
}

createMenu("Foo", "Bar", "Baz", true);

// good:
function createMenu({ title, body, buttonText, cancellable }) {
  // ...
}

createMenu({
  title: "Foo",
  body: "Bar",
  buttonText: "Baz",
  cancellable: true
});
```

Functions should do one thing
```javascript
//bad:
function emailClients(clients) {
  clients.forEach(client => {
    const clientRecord = database.lookup(client);
    if (clientRecord.isActive()) {
      email(client);
    }
  });
}

//good:
function isActiveClient(client) {
  const clientRecord = database.lookup(client);
  return clientRecord.isActive();
}

function emailActiveClients(clients) {
  clients.filter(isActiveClient).forEach(email);
}
```

Function names should say what they do
```javascript
//bad:
function addToDate(date, month) {
  // ...
}

const date = new Date();

// It's hard to tell from the function name what is added
addToDate(date, 1);

// good:
function addMonthToDate(month, date) {
  // ...
}

const date = new Date();
addMonthToDate(1, date);
```

Functions should only be one level of abstraction.
A functions operates at a specific level of abstraction:
- High-level abstraction: Describe *what* or *why* (domain-specific 
  actions).
- Low-level abstraction: Describe *how* (technical details of step-by-step 
  instructions).
```javascript
// bad:
function parseBetterJSAlternative(code) {
  const REGEXES = [
    // ...
  ];

  const statements = code.split(" ");
  const tokens = [];
  REGEXES.forEach(REGEX => {
    statements.forEach(statement => {
      // ...
    });
  });

  const ast = [];
  tokens.forEach(token => {
    // lex...
  });

  ast.forEach(node => {
    // parse...
  });
}

// good:
function parseBetterJSAlternative(code) {
  const tokens = tokenize(code);
  const syntaxTree = parse(tokens);
  syntaxTree.forEach(node => {
    // parse...
  });
}

function tokenize(code) {
  const REGEXES = [
    // ...
  ];

  const statements = code.split(" ");
  const tokens = [];
  REGEXES.forEach(REGEX => {
    statements.forEach(statement => {
      tokens.push(/* ... */);
    });
  });

  return tokens;
}

function parse(tokens) {
  const syntaxTree = [];
  tokens.forEach(token => {
    syntaxTree.push(/* ... */);
  });

  return syntaxTree;
}
```

Remove duplicate code.
Bad abstractions can be worse than duplicate code.
```javascript
// bad:
function showDeveloperList(developers) {
  developers.forEach(developer => {
    const expectedSalary = developer.calculateExpectedSalary();
    const experience = developer.getExperience();
    const githubLink = developer.getGithubLink();
    const data = {
      expectedSalary,
      experience,
      githubLink
    };

    render(data);
  });
}

function showManagerList(managers) {
  managers.forEach(manager => {
    const expectedSalary = manager.calculateExpectedSalary();
    const experience = manager.getExperience();
    const portfolio = manager.getMBAProjects();
    const data = {
      expectedSalary,
      experience,
      portfolio
    };

    render(data);
  });
}

// good:
function showEmployeeList(employees) {
  employees.forEach(employee => {
    const expectedSalary = employee.calculateExpectedSalary();
    const experience = employee.getExperience();

    const data = {
      expectedSalary,
      experience
    };

    switch (employee.type) {
      case "manager":
        data.portfolio = employee.getMBAProjects();
        break;
      case "developer":
        data.githubLink = employee.getGithubLink();
        break;
    }

    render(data);
  });
}
```

Don't use flags as functions parameters, flags tell your user that this 
function does more than one thing. Functions should do one thing.
```javascript
// bad:
function createFile(name, temp) {
  if (temp) {
    fs.create(`./temp/${name}`);
  } else {
    fs.create(name);
  }
}

// good:
function createFile(name) {
  fs.create(name);
}

function createTempFile(name) {
  createFile(`./temp/${name}`);
}
```

Avoid Side Effects
A function produces a side effect if it does anything other than take a 
value in and return another value or values. A side effect could be writing
to a file, modifying some global variable, or accidentally wiring all your 
money to a stranger.
Now, you do need to have side effects in a program on occasion.
What you want to do is to centralize where you are doing this. Don't have 
several functions and classes that write to a particular file. Have one 
service that does it. One and only one.
he main point is to avoid common pitfalls like sharing state between 
objects without any structure, using mutable data types that can be written
to by anything, and not centralizing where your side effects occur.
```javascript
// bad:
// Global variable referenced by following function.
// If we had another function that used this name, now it'd be an array and
// it could break it.
let name = "Ryan McDermott";

function splitIntoFirstAndLastName() {
  name = name.split(" ");
}

splitIntoFirstAndLastName();

console.log(name); // ['Ryan', 'McDermott'];

// good:
function splitIntoFirstAndLastName(name) {
  return name.split(" ");
}

const name = "Ryan McDermott";
const newName = splitIntoFirstAndLastName(name);

console.log(name); // 'Ryan McDermott';
console.log(newName); // ['Ryan', 'McDermott'];
```

Some values are mutable (e.g.: maps, arrays) and some other are immutable 
(e.g.: primitive values).
To avoid creating side effects, you should consider clonning your mutable 
objects and making changes to it instead of making changes to the provided 
data. Cloning big objects can be very expensive in terms of performance. 
Luckily, this isn't a big issue in practice because there are great 
libraries like [Immutable.js](https://immutable-js.com/) that allow this 
kind of programming approach to be fast and not as memory intensive as it 
would be.
```javascript
// bad:
const addItemToCart = (cart, item) => {
  cart.push({ item, date: Date.now() });
};

// good:
const addItemToCart = (cart, item) => {
  return [...cart, { item, date: Date.now() }];
};
```

Favor functional programming over imperative programming, functional 
languages can be cleaner and easier to test.
```javascript
const programmerOutput = [
  {
    name: "Uncle Bobby",
    linesOfCode: 500
  },
  {
    name: "Suzie Q",
    linesOfCode: 1500
  },
  {
    name: "Jimmy Gosling",
    linesOfCode: 150
  },
  {
    name: "Gracie Hopper",
    linesOfCode: 1000
  }
];

// bad:
let totalOutput = 0;

for (let i = 0; i < programmerOutput.length; i++) {
  totalOutput += programmerOutput[i].linesOfCode;
}

// good:
const totalOutput = programmerOutput.reduce(
  (totalLines, output) => totalLines + output.linesOfCode,
  0
);
```

Encapsulate conditional
```javascript
// bad:
if (fsm.state === "fetching" && isEmpty(listNode)) {
  // ...
}

// good:
function shouldShowSpinner(fsm, listNode) {
  return fsm.state === "fetching" && isEmpty(listNode);
}

if (shouldShowSpinner(fsmInstance, listNodeInstance)) {
  // ...
}
```

Avoid negative conditionals
```javascript
// bad:
function isDOMNodeNotPresent(node) {
  // ...
}

if (!isDOMNodeNotPresent(node)) {
  // ...
}

// good:
function isDOMNodePresent(node) {
  // ...
}

if (isDOMNodePresent(node)) {
  // ...
}
```

Avoid conditionals
You can use polymorphism to achieve the same behaviour as an if statement in many cases.
Using if statements tells the user that your code does more than one thing.
```javascript
// bad:
class Airplane {
  // ...
  getCruisingAltitude() {
    switch (this.type) {
      case "777":
        return this.getMaxAltitude() - this.getPassengerCount();
      case "Air Force One":
        return this.getMaxAltitude();
      case "Cessna":
        return this.getMaxAltitude() - this.getFuelExpenditure();
    }
  }
}

// good:
class Airplane {
  // ...
}

class Boeing777 extends Airplane {
  // ...
  getCruisingAltitude() {
    return this.getMaxAltitude() - this.getPassengerCount();
  }
}

class AirForceOne extends Airplane {
  // ...
  getCruisingAltitude() {
    return this.getMaxAltitude();
  }
}

class Cessna extends Airplane {
  // ...
  getCruisingAltitude() {
    return this.getMaxAltitude() - this.getFuelExpenditure();
  }
}
```

Avoid type checking between classes, instead consider a more consistent 
API.
```javascript
// bad:
function travelToTexas(vehicle) {
  if (vehicle instanceof Bicycle) {
    vehicle.pedal(this.currentLocation, new Location("texas"));
  } else if (vehicle instanceof Car) {
    vehicle.drive(this.currentLocation, new Location("texas"));
  }
}

// good:
function travelToTexas(vehicle) {
  vehicle.move(this.currentLocation, new Location("texas"));
}
```

Remove dead code, it'll be safe in your version history if you still need 
it.
```javascript
// bad:
function oldRequestModule(url) {
  // ...
}

function newRequestModule(url) {
  // ...
}

// good:
const req = newRequestModule;
inventoryTracker("apples", req, "www.inventory-awesome.io");

function newRequestModule(url) {
  // ...
}

const req = newRequestModule;
inventoryTracker("apples", req, "www.inventory-awesome.io");
```

## Objects and Data Structures
Use getters and setters
- When you want to do more beyond getting an object property, you don't 
  have to look up and change every accessor in your codebase.
- Encapsulates the internal representation.
```javascript
// bad:
function makeBankAccount() {
  // ...

  return {
    balance: 0
    // ...
  };
}

const account = makeBankAccount();
account.balance = 100;

// good:
function makeBankAccount() {
  // this one is private
  let balance = 0;

  // a "getter", made public via the returned object below
  function getBalance() {
    return balance;
  }

  // a "setter", made public via the returned object below
  function setBalance(amount) {
    // ... validate before updating the balance
    balance = amount;
  }

  return {
    // ...
    getBalance,
    setBalance
  };
}

const account = makeBankAccount();
account.setBalance(100);
```

Make objects have private members
```javascript
// bad:
class Person {
    name = "John Doe"
}

const person = new Person();
delete person.name;

// good:
class Person {
    #name = "John Doe"
}

const person = new Person();
// can't access #name outside the scope of the class.
```

## Classes
Use method chaining, it allow your code to be expressive and less verbose 
by applying imperative programming.
```javascript
// bad:
class Car {
  constructor(make, model, color) {
    this.make = make;
    this.model = model;
    this.color = color;
  }

  setMake(make) {
    this.make = make;
  }

  setModel(model) {
    this.model = model;
  }

  setColor(color) {
    this.color = color;
  }

  save() {
    console.log(this.make, this.model, this.color);
  }
}

const car = new Car("Ford", "F-150", "red");
car.setColor("pink");
car.save();

// good:
class Car {
  constructor(make, model, color) {
    this.make = make;
    this.model = model;
    this.color = color;
  }

  setMake(make) {
    this.make = make;
    // NOTE: Returning this for chaining
    return this;
  }

  setModel(model) {
    this.model = model;
    // NOTE: Returning this for chaining
    return this;
  }

  setColor(color) {
    this.color = color;
    // NOTE: Returning this for chaining
    return this;
  }

  save() {
    console.log(this.make, this.model, this.color);
    // NOTE: Returning this for chaining
    return this;
  }
}

const car = new Car("Ford", "F-150", "red").setColor("pink").save();
```

Prefer composition over inheritance, you should use inheritance when:
- Your inheritance represents an "is-a" relationship and not a "has-a" 
  relationship.
- You can reuse code from the base classes .
- You want to make global changes to derived classes by changing a base 
  class.
```javascript
class Employee {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }

  // ...
}

// Bad because Employees "have" tax data. EmployeeTaxData is not a type of 
// Employee
class EmployeeTaxData extends Employee {
  constructor(ssn, salary) {
    super();
    this.ssn = ssn;
    this.salary = salary;
  }

  // ...
}

// good:
class EmployeeTaxData {
  constructor(ssn, salary) {
    this.ssn = ssn;
    this.salary = salary;
  }

  // ...
}

class Employee {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }

  setTaxData(ssn, salary, TaxData) {
    this.taxData = new TaxData(ssn, salary)
  }
  // ...
}
```

## Testing
The main point is to just make sure you are reaching your coverage goals 
before launching any feature, or refactoring an existing one.

Single concept per test
```javascript
// bad:
import assert from "assert";

describe("MomentJS", () => {
  it("handles date boundaries", () => {
    let date;

    date = new MomentJS("1/1/2015");
    date.addDays(30);
    assert.equal("1/31/2015", date);

    date = new MomentJS("2/1/2016");
    date.addDays(28);
    assert.equal("02/29/2016", date);

    date = new MomentJS("2/1/2015");
    date.addDays(28);
    assert.equal("03/01/2015", date);
  });
});

// good:
import assert from "assert";

describe("MomentJS", () => {
  it("handles 30-day months", () => {
    const date = new MomentJS("1/1/2015");
    date.addDays(30);
    assert.equal("1/31/2015", date);
  });

  it("handles leap year", () => {
    const date = new MomentJS("2/1/2016");
    date.addDays(28);
    assert.equal("02/29/2016", date);
  });

  it("handles non-leap year", () => {
    const date = new MomentJS("2/1/2015");
    date.addDays(28);
    assert.equal("03/01/2015", date);
  });
});
```

## Formatting
Function callers and callees should be close. If a function calls another, 
keep those functions vertically close in the source file.
We tend to read code from top-to-bottom, like a newspaper. Because of this,
make your code read tha way.
```javascript
// bad:
class PerformanceReview {
  constructor(employee) {
    this.employee = employee;
  }

  lookupPeers() {
    return db.lookup(this.employee, "peers");
  }

  lookupManager() {
    return db.lookup(this.employee, "manager");
  }

  getPeerReviews() {
    const peers = this.lookupPeers();
    // ...
  }

  perfReview() {
    this.getPeerReviews();
    this.getManagerReview();
    this.getSelfReview();
  }

  getManagerReview() {
    const manager = this.lookupManager();
  }

  getSelfReview() {
    // ...
  }
}

const review = new PerformanceReview(employee);
review.perfReview();

// good:
class PerformanceReview {
  constructor(employee) {
    this.employee = employee;
  }

  perfReview() {
    this.getPeerReviews();
    this.getManagerReview();
    this.getSelfReview();
  }

  getPeerReviews() {
    const peers = this.lookupPeers();
    // ...
  }

  lookupPeers() {
    return db.lookup(this.employee, "peers");
  }

  getManagerReview() {
    const manager = this.lookupManager();
  }

  lookupManager() {
    return db.lookup(this.employee, "manager");
  }

  getSelfReview() {
    // ...
  }
}

const review = new PerformanceReview(employee);
review.perfReview();
```

## Comments
Only comment things that have business logic complexity. Comments are an 
apology, not a requirement. Good code mostly documents itself.
```javascript
// bad:
function hashIt(data) {
  // The hash
  let hash = 0;

  // Length of string
  const length = data.length;

  // Loop through every character in data
  for (let i = 0; i < length; i++) {
    // Get character code.
    const char = data.charCodeAt(i);
    // Make the hash
    hash = (hash << 5) - hash + char;
    // Convert to 32-bit integer
    hash &= hash;
  }
}

// good:
function hashIt(data) {
  let hash = 0;
  const length = data.length;

  for (let i = 0; i < length; i++) {
    const char = data.charCodeAt(i);
    hash = (hash << 5) - hash + char;

    // Convert to 32-bit integer
    hash &= hash;
  }
}
```
