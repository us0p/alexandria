# Testing
Nest includes features such as the following to help developers and teams 
build and automate tests. Nest:
- automatically scaffolds default unit tests for components and e2e tests 
  for applications
- provides default tooling (such as a test runner that builds an isolated 
  module/application loader)
- provides integration with Jest and Supertest out-of-the-box, while 
  remaining agnostic to testing tools
- makes the Nest dependency injection system available in the testing 
  environment for easily mocking components

You can use any testing framework that you like, as Nest doesn't force any 
specific tooling. Simply replace the elements needed (such as the test 
runner), and you will still enjoy the benefits of Nest's ready-made testing
facilities.

Keep your test files located near the classes they test. Testing files 
should have a .spec or .test suffix.
