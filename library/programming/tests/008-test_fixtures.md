# Test Fixtures
A test fixture is a fixed state of a set of objects used as a baseline for running test.
A software test fixture sets up the system for the testing process by providing the initialization code satisfying whatever preconditions there may be an example could be loading up a database with known parameters from a customer site before running your test.

Test fixtures allow for tests to be repeatable since you start with the same setup every time.
Preconfigures tests into a known state at start instead of working from a previous test run.
The purpose of a test fixture is to ensure that there is a well known and fixed environment in which tests are tun so that results are repeatable.

A fixture encompasses everything necessary to establish the state required for testing the SUT. In the context of Test Automation, it's the setup phase of the test.
## Test Fixtures
- Stablishes an initial state before or after running tests.
- Runs tests in isolation.
- Ensures repeatable results.
- If you need to provide data to your fixtures, it's common to create a folder named "fixtures" and add the data inside it in any file format deemed acceptable. It makes clear that files inside that folder are related to fixtures.