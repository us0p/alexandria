## Unit
- You should only unit test business rules.
- It's a good call to unit test complex problems or things that are too hard to test manually. using tests to drive correctness of complex problems and to automate complex manual testing can save a lot of time.
- Unit tests tend to break as implementation change and make refactor hard. doesn't catch bugs of interactions with other code. often thrown away when code change.
- Unit tests are tests that provide value in the short time but can become a debt as the projects lives on.
- If you want your unit tests to have value for more time you should focus on black box testing, test functions and methods based on their contracts and not their implementations this will make the test more valuable as long as the interface doesn't change.
- Many errors related to unit testing that get through are errors of assumption.
## Mocking
- Split your code to separate rules from external systems to avoid mocking in excess.
```typescript
import fs from "node:fs/promises"

// Bad: requires mocking fs.readFile as it's an external dependency
async function processFile(filePath: string): Promise<string> {
	const fileContent = await fs.readFile(filePath);
	// processing...
}

// ----------------------------------------------------------------

// Good: extracted external dependency allowing dependency injection.
async function getFileContent(filePath: string): Promise<string> {
	return fs.readFile(filePath)
}

function processFileContent(fileContent: string): string {
	// same processing...
}

const fileContent = await getFileContent("./someFile.txt");
const processedFileContent = processFileContent(fileContent);
```
## TDD
- Avoid testing things you don't know the expected behavior, or what it should do, tests can be used to drive the design and implementation of something that you know the behavior.
- Tdd is specially good for regression tests, when you find a bug, you first write the test that reproduces the bug and then fixes it.
## Integration
- When you're working in a distributed architecture, running integration or e2e tests can become a very complicated thing as you need all the other services available and in the same stage as your code as well (dev, staging, etc).
- E2E tests provide an overall understanding of the system and provide more value in the long time but can be hard to understand and can become a clumsy test that are often ignored.
- Integration tests is a high level testing of the system that doesn't test a complete segment of the system, it just tests the integration of the components. It can test the correctness of the system with access to low level details and is easy to see what break.
- Integration tests is better done when system start to stabilize.
- Integration tests remain valuable for longer.
- Should focus e2e tests on most common and important features and edge cases, but not too many or they become impossible to maintain and then possibly ignored.
## Testing in general
- Some people prefer to write tests before the prototype phase, when code has begun to firm up and contracts and interfaces are more stable.
- The best tests are the ones that are deeply on the context of the problem that they are testing.
- If something is fragile and you write tests to make it more robust to failure, you should probably focus your effort in rewriting the core first to make it more robust as the problem is probably in the code and not in the functionality.
- Thinking about functions that are just wrappers around native or library functions. The test should look at the expected behavior and not to the implementation. If you hide the details of your function, no one could know which library or native function you're using. So it makes sense to create tests to validate the behavior. So we can change the implementation and guarantee that the behavior still the same. There're many ways to produce a certain result, but the result is only one.