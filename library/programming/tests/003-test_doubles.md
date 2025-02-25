# Test Doubles
Are objects used to isolate parts of a system for testing. Each object has a distinct objective and purpose:
## Dummy
Never actually used, they are just used to fill parameter lists.
## Fake
Actually have working implementation, but usually take some shortcut which makes them not suitable for production (e.g. InMemoryDatabase).
## Stubs
Provide default answers to calls made during the test, usually not responding at all to anything outside what's programmed.
## Spies
Are stubs that also record some information based on how they were called.
## Mocks
Pre-programmed with expectations which form a specification of the calls they are expected to receive. They can throw an exception if they receive a call they don't expect and are checked during verification to ensure they got all the calls they were expecting.