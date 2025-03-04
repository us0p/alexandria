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
- Not concerned with the internal workings of the system. It observes how the system behave, from the user's point of view.
- Great for integration testing.
- Uses a syntax both developers and stakeholders can easily understand.
- Tests the behavior of the system from the `outside in`.
- It's a higher level of testing.
- Ensures that you're building the "right thing".
- The appropriate levels for performing BDD are integration, system, and acceptance testing.
- Notations are closer to everyday language than TDD.
- Most commonly used syntax in BDD is called Gherkin.
- BDD specification describer how the system should behave in a situation.
- Tools afford the automatic generation of technical documentation from specifications. Thus documentation is always in sync with what you're building.
- You can generate tests directly from the BDD specification.
- BDD specification includes features and scenarios.
- Features represent use stories.
- You can have as many features as needed. Usually each feature has its own specification file.
- Each feature contains one or more concrete examples, or scenarios which describes a single behavior of the feature by using the Gherkin syntax.
- Each scenarios formulates a complete test case.
- Backgrounds are used to share a given context between multiple features. It's translated into a test fixture that you can use to specify the context once and then establish it before every scenario in the feature.
- Typically you use background with one or more Given statements to set up the initial testing state.
- Always write the feature files as if you were explaining how to use the feature not what the feature does undercovers.
- Step files are source code files containing functions that match the Gherkin statements in the feature file.
- Note that you don't have to make any assertion in a given step as each step is just one part of a test case, it's not an entire test case. One step may be to set something up, like a state, and the following step asserts something about that state.
### Feature Syntax
Template example
```plaintext
Feature: <title>

As a <role>
I want <functionality>
So that <benefit>

Background:
	Given <condition>
		# Representation of a table which represents the format of data 
		# that should be present before each scenario.
		| column_name | column_name |
		| data        | data        |
		| data        | data        |
		| ...         | ...         |

Scenario 1: <scenario title>
	<Gherkin syntax>
```

Concrete example
```plaintext
Feature: Returns go to stock

As a store owner
I want to add items back to stock when they're returned
So that I can keep track of stock

Scenario 1: Refunded items shold be returned to stock
	Given that a customer previously bought a black sweater from me
	And I have three black sweaters in stock
	When they return the black sweater for a refund
	Then I should have four black sweaters in stock

Scenario 2: Exchanged items should be returned to stock
	Given that a customer previously bought a blue shirt from tme
	And I have two blue shirts in stock
	And I have three black shirts in stock
	When they exchange the blue shirt for a replacement in black
	Then I should have three blue shirts in stock
	And I should have two black shirts in stock
```
### Gherkin syntax
In this syntax, every example has at least three lines, referred to as steps. Each step starts with a keyword. This syntax is commonly used as `Given, When, Then`.
- **Given**: Conditions required to put the system into the state needed to perform the tests.
- **When**: Actions that the user takes to interact with the system under test.
- **Then**: Expected outcome of the actions that the user performs.
To improve readability, you can also use the `And, But` keywords instead of chaining the base keywords.
- **And**: Always take on the meaning of the previous base keyword that comes before it.
- **But**: State what should not occur.
In the description of each step, any double quoted term is used to represent something that should be present in the behavior.
```plaintext
Feature: Search for pets by category

As a pet shop customer
I need to be able to search for a pet by category
So that I only see the category of pet i'm interested in buying

Background
	Given the following pets
		| name  | category | available |
		| Fido  | dog      | True      |
		| Kitty | cat      | True      |
		| Leo   | lion     | False     |

Scenario: Search for dogs
	Given I am on the "Home Page"
	When I set the "Category" to "dog"
	And I click the "Search" button
	Then I should see the message "Success"
	And I should see "Fido" in the results
	But I should not see "Kitty" in the results
	And I should not see "Leo" in the results

# The following scenarion gives some information:
# 1. It must have a page with the title "Home Page"
# 2. The page must have a field with text "Category" that accepts the input "dog"
# 3. The page must have a button the with the text "Search"
# 4. When the button is clicked it should render a cue with the text "Success" 
# 5. The page should contain the data for a dog named "Fido"
# 6. The page shouldn't display information for a cat named "Kitty"
# 7. The page shouldn't display information for a lion named "Leo"
```
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