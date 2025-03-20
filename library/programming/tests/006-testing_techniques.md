## White Box
Software's internal structure, design, and coding are tested to verify input-output flow and improve design, usability and security.
This approach can be done at any level of software development system, integration or unit.
This approach requires understanding of the inner code or at least the intent.
Looks for:
- Internal security holes
- Broken or poorly structured paths in the coding process
- The flow of specific inputs through the code
- Expected output
- The functionality of conditional loops
- Testing of each statement, object, and function on an individual basis
## Code Coverage
Is a technique in which the tests are created execute all the lines of the code. It also include some different coverage techniques.
- statement coverage: test that each line in the code is called.
- branch coverage: test that each condition in the code is executed, 100% branch coverage  means 100% statement coverage but not the opposite.
## Test Coverage
The percentage of lines of code executed during tests. It reveal which lines of code were not tested. Even with 100% test coverage your code can still have bugs.
## Boundaries
Tests how the code performs when input values are in the boundaries or extreme values.

-------
## Black Box
software is tested without having knowledge of internal code structure, implementation details and internal paths. Mainly focuses on input and output of software and it's entirely based on software requirements and specifications. It's also known as Behavioral Testing.
## Equivalente Partitioning
Input values are divided into different classes based on its similarity in the outcome. Instead of using each and every input value, we can now use any value from the class to test the outcome. Helps maintaining coverage while reducing the amount of rework.
![[Pasted image 20250225104948.png]]
## Boundary Value
Focus on the values at boundaries as it is found that many applications have a high amount of issues on the boundaries. Also ensures that any value in the testing range is valid/invalid.
## Decision Table
If there's conditions, the tester should identify the output for each condition and create a table that relates an input with the desired output for each condition.
## Table Driven Tests
Each table entry is a complete test case with inputs and expected results, and additional information such as the test name to make the test output easily readable.
Given a table of tests, the actual test simply iterates through all table entries and for each entry performs the necessary tests. The test code is written once and amortized over all table entries, so it makes sense to write a careful test with good error messages.