## Software testing levels
### Unit tests
lowest level of unit testing, where you test individual units of the system independently. It's implemented by a single developer during its development process. You want the "happy" and "sad" patsh to test all the paths or behaviours of your code. This is the level where you perform Test Driven Development (?).
### Integration Testing
Combine individual units to test them as a group looking to expose flaws between integrated units. This is the level where you perform Behaviour Driven Development (?), you test to check if the behaviour between the units. This tests are probably performed in a development environment.
### System Testing
The entire software is tested, integrating all the modules in the system. The goal is to evaluate the system compliance with the specific requirements and to make sure the whole system works together. This stage of testing you probably moved into a pre-production environment that's more like production making sure everything works togheter.
### Acceptance tests
Pourpose is to evaluate the compliance with business requirements and assess wheter it's acceptable for delivery. This test is done by the end user. before they can say "yes, i accept the system". Usually perform in the same environment as the system testing.
## BDD and TDD
### BDD
- Focuses on the behaviour of the system from the outside.
- Great for integration testing.
- Uses a syntas both developers and stakeholders can easily understand.
- Tests the behavior of the system from the `outside in`.
- It's a higher level of testing.
- Ensures that you're building the "right thing".
### TDD
- Focuses on how the system works from the inside.
- Test drive the design.
- You write the test first then you write the code to make the tests pass.
- Keeps you focused on the purpose of the code.
- Tests the functions of the system from the `inside out`.
- It's a lower level of testing.
- Ensures that you're building the "thing right".
- Ensures that future code doesn't break your code.
- In order to create a DevOps CI/CD pipeline, all testing must be automated.
- Write test cases based on the requirements.
## TDD workflow
![[Pasted image 20250302114401.png]]
## Defensive programming
Is when you write your code expecting it to fail, then you add defenses, to prevent the code from failing in those cases.
## Glossary
- CI: Continuous integration is the tests that run in the CI server when you integrate your code to let you know if you broke something.
- Test cases: Help you and others know what works, what doesn't, and how to call the code. They serve as examples for using the code.
## Anatomy of a test case
- Test fixtures help developers create an initial testing state
- Testing frameworks provide tools that simplify testing conditions
- Test cases include assertions that verify that the code behaves as expected.
## Test Fixtures
- Stablishes an initial state before or after running tests.
- Runs tests in isolation.
- Ensures repeatable results.
- If you need to provide data to your fixtures, it's common to create a folder named "fixtures" and add the data inside it in any file format deemed acceptable. It makes clear that files inside that folder are related to fixtures.
## Test Coverage
The percentage of lines of code executed during tests. It reveal which lines of code were not tested. Even with 100% test coverage your code can still have bugs.
## Factories and fakes
Factories and fakes are used to create fake data and fake instances of objects so that you can use as realistic tests data on your tests, often you want to do this when you need to create many different data and don't want to do this manually.
For JavaScript you can use [Faker.js](https://fakerjs.dev/).
## Mocking
Process for creating objects that mimic the behavior of real objects. Used to replace external systems or objects that you system depends on and create repeatable results.
### Mock patching
Allows you to change the behavior of a function call, it's specially usefull if the function is not under your control. Also usefull when you want to simulate error conditions but you can't actually cause those errors while under test.
It's a mocking technique by which developers change the behavior of a function call.
You can patch a function in two ways:
- Patching its return value.
- Replacing a function with another function, a.k.a. side effect.
### Mock object
Is an object that simulates the behavior of a real object in ways that you can control. Use mock sparingly, make sure you're testing your code and not your mocks.