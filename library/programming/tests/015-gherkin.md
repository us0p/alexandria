# Gherkin
## Overview
In this syntax, every feature has one or more scenarios which has at least three lines, referred to as steps. Each step starts with a keyword. This syntax is commonly used as `Given, When, Then`.
- **Given**: Conditions required to put the system into the state needed to perform the tests.
- **When**: Actions that the user takes to interact with the system under test.
- **Then**: Expected outcome of the actions that the user performs.
To improve readability, you can also use the `And, But` keywords instead of chaining the base keywords.
- **And**: Always take on the meaning of the previous base keyword that comes before it.
- **But**: State what should not occur.
In the description of each step, any double quoted term is used to represent something that should be present in the behavior.

Features represent use stories and you can have as many features as needed. Usually each feature has its own specification file.
Always write the feature files as if you were explaining how to use the feature not what the feature does undercover.

Each scenario should describe a single and complete behavior of the feature.

Backgrounds are used to share a given context between multiple scenarios. It's translated into a test fixture that you can use to specify the context once and then establish it before every scenario in the feature. 
Typically you use background with one or more Given statements to set up the initial testing state.

The actual code which implements the steps defined in the feature files is in the step files and they match the Gherkin statements in the feature file.
 Note that you don't have to make any assertion in a given step as each step is just one part of a test case, it's not an entire test case. One step may be to set something up, like a state, and the following step asserts something about that state.
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