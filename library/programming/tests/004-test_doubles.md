# Test Doubles
Any kind of object used in place of a real object for testing purposes. Are used to isolate parts of a system for testing.
## Dummy
Never actually used, they are just used to fill parameter lists.
## Fake
Actually have working implementation, but usually take some shortcut which makes them not suitable for production (e.g. InMemoryDatabase).
## Stubs
Provide default answers to calls made during the test, usually not responding at all to anything outside what's programmed.
## Spies
Are stubs that also record some information based on how they were called.
## Mocks
Pre-programmed with expectations which form a specification of the calls they are expected to receive. They ensure they received all the calls they were expecting  with all the required parameters. They enforce the behavior of the mocked object.

## Difference between Mocks and other test doubles
Mocks uses behavior verification while other test doubles often uses state verification but can also use behavior testing.

Other test doubles often include extra methods to validate the state of the objects after the execution, which is then used to assert the success or failure of the test.

The mock only cares for the behavior, rather to what state it should be.
## Mock and Fake example
```typescript
import assert from "node:assert"
import {it} from "node:test"
import Mock from "fictious-mock-library"

class Order {
	//...
}

class MailService {
	//...
}

class MailServiceFake {
	messages: string[] = [];
	send(message: string) {
		this.messages.push(message)
	}
	numberSent() {
		return this.message.length
	}
}

// Fake example
it("should test email sending with spy", () => {
	const order = new Order("item", 1);
	const mailer = new MailServiceStub()
	order.setMailer(mailer)
	order.fill({})
	assert.strictEqual(1, mailer.numberSent())
})

// Mock example
it("should test email sending with mock", () => {
	const order = new Order("item", 1);
	const mailer = new Mock(MailService)
	order.setMailer(mailer)
	order.fill({})
	assert.strictEqual(mailer.send.callCount(), 1)
	assert.deepStrictEqual(
		mailer.send.arguments(),
		{email: null, subject: "failed order"}
	)
})
```