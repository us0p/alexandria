# Behavior Driven Development (BDD)
## Overview
Behavior Driven Development (BDD) is an evolution of Test Driven Development (TDD). Its main goal is to involve non-technical stakeholders in understanding the testing functionalities of programs. As a result, test scenarios are not only written by the software team but also involve collaboration between developers, quality assurance teams, and business people.

BDD focuses on the **language and interaction** used during software development. Developers use a combination of their **native language and ubiquitous language**, allowing them to focus on **why** the code must be created rather than the technical details. This minimizes the gap between technical and domain-specific language.
## How BDD Works
BDD makes use of a **Domain Specific Language (DSL)**, which converts structured natural language statements into executable tests. 

In simple terms, BDD consists of having **all interested parties collaborate** to define application requirements using a shared language, in the form of **user stories and scenarios**.
Developers can then:
1. Use these specifications to create automated tests.
2. Write production code to pass the tests.
## Focus Areas in BDD
BDD helps define:
- Where to start the process.
- What to test and what not to test.
- How much needs to be tested at once.
- How to understand why a test fails.
### Writing Scenarios in BDD
In BDD, the process starts by **describing acceptance criteria** for software requirements in the form of **scenarios**. These scenarios follow a structured template:

```plaintext
Given some initial context,
When an event occurs,
Then ensure some outcomes.
```
Sometimes, the relation between the code and the expected behavior can be more explicit:
```typescript
import {it} from "node:test"
import assert from "node:assert"

it("should be an example of BDD", () => {
	// Given
	const list = new Array()

	// When
	list.push(1)

	// Then
	assert.strictEqual(list.length, 1)
})
```
## Advantages of BDD
- **Dynamic documentation:** The system is more easily documented.
- **Example-based approach:** Uses examples to describe the behavior of an application or a code unit.
## Origins of BDD

BDD was originally developed by **Daniel Terhorst-North** as a technique to help people learn **Test Driven Development (TDD)** by focusing on how TDD operates as a **design technique**.

This led to:

- Renaming **tests** as **behaviors** to emphasize **what** an object needs to do rather than how it does it.
- Talking about **specifications** instead of test cases.
- Using **scenarios** instead of tests.

BDD specifications should **describe what people want to do with the software**, not how they will achieve it. This abstraction makes behavior clearer without focusing on implementation details, making BDD an effective tool for documentation and a stable source of information that doesn’t change as often as implementation details.
### When using BDD
- Think about testing your software based on the **behavior it exhibits to a user**, rather than focusing on the internal structure from the producer’s perspective.
- The specifications should **not** describe how the software works internally. Instead, they should **describe small increments in functionality** from a user's point of view.
- These specifications are backed by **sets of examples** that serve as **acceptance criteria**. If these criteria are met, the system is considered to be doing something useful.

---
# Test Driven Development (TDD)
## Overview
TDD is a software development approach where **test cases are written first** to drive the implementation of the software toward the expected behavior.

There are two techniques for writing tests:
1. **White-box testing** – Ensures the implementation follows certain criteria to avoid bugs.
2. **Black-box testing** – Specifies the expected behavior of the implementation.
## Key Principles of TDD
- Tests must be **written before the actual implementation**.
- This drives the **design and structure** of the code, making it more modular.
- When tests are written **after** the code, the code often becomes harder to test, leading to **poor design** and **tight coupling** between tests and the system under test (SUT), breaking the principle of **encapsulation**.

TDD is essentially a software development approach in which test cases are developed to **specify and validate** what the code will do.
## TDD Cycle
1. **Write a test**
2. **Make it run**
3. **Refactor**
4. **Repeat**
## Acceptance TDD (ATDD)
- **Acceptance TDD (ATDD)** involves writing a **single acceptance test** that:
    - Fulfills a requirement from the specification.
    - Satisfies the expected behavior of the system.
- After writing the test, only **enough production code** is written to make the test pass.
- Acceptance tests focus on the **overall behavior of the system**.

ATDD was also known as **Behavior Driven Development (BDD)** because of its emphasis on **specifications** and **behavioral expectations** rather than technical implementation details.