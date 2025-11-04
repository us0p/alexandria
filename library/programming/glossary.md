# Pure Function
Specific type of function that:
- It takes some input and returns an output.
- It doesn't cause any observable side effects, such as modifying the state of the system or interacting with external sources.
- Given the same input, it will always return the same output.
- It doesn't depend on any state or variables that are outside of its scope.

Pure functions are considered to be more predictable and easier to test, as their behavior is determined solely by the input they receive and their internal logic.

They also make it easier to reason about the behavior of a program, since the output of a pure function is not affected by any external factors.
# Cyclomatic Complexity
Measures how many independent paths exist through a piece of code. 

>"How many different routes could the program take through this logic?"

The more paths there are, the harder it is to reason about, test, and maintain that code.

It also giver a **lower bound** for the number of test cases required for full *branch coverage*.

```python
def process(data):
    if not data:
        return
    for item in data:
        if item > 0 and item < 100:
            print(item)
```

The code above has a Cyclomatic Complexity of 5:
- The linear path
- First `if`
- `for` loop
- Inner `if`
- `and` condition

Which means that this function can be executed in 5 different ways. Also, it means that it would take at least 5 different test cases to test all branches in that function.

Notice that high complexity means you need more test cases to ensure correctness.