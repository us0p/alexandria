Testing Serverless funtion and applications

A serverless application architecture includes managed services that 
provide critical application functionality through API calls. For this 
reason, your development cycle should include automated tests that verify 
functionality when your function and services interact.
If you do not create cloud-based tests, you could encounter issues due to 
differences between your local environment and the deployed environment. 
Your continuous integration process should run tests against a suite of 
resources provisioned in the cloud before promoting your code to the next 
deployment environment, such as QA, Staging, or Production.

We recommend adopting a testing strategy that tests managed service 
behaviors, cloud configuration, security policies, and the integration with
your code to improve software quality. Behavior testing, also known as 
black box testing, verifies a system works as expected without knowing all 
the internals. 
- Run unit tests to check business logic inside Lambda functions.
- Verify integrated services are actually invoked, and input parameters are
  correct.
- Check that an event goes through all expected services end-to-end in a 
  workflow.
Some application functionality can be delegated entirely to managed 
services such as Amazon S3, or created without using any internally 
developed code. There is no need to test these managed services, but you do
need to test the integration with these services. 

Serverless solutions are built from your function code and cloud-based 
managed services, such as queues, databases, event buses, and messaging 
systems. These components are all connected through an event-driven 
architecture, where messages, called events, flow from one resource to 
another. These interactions can be synchronous, such as when a web service 
returns results immediately, or an asynchronous action which completes at a
later time, such as placing items in a queue or starting a workflow step. 
Your testing strategy must include both scenarios and test the interactions
between services. For asynchronous interactions, you may to need detect 
side effects in downstream components that may not be immediately 
observable.

Testing Techniques
- Testing in the cloud: you deploy infrastructure and code to test with 
  actual services, security policies, configurations and infrastructure 
  specific parameters. Cloud-based tests provide the most accurate measure 
  of quality of your code.
  Debugging a function in the console is a quick way to test in the cloud. 
  To automate testing in the development and build lifecycle, you will need
  to test outside of the console.
- Testing with mocks (also called fakes): A fake is a mock implementation 
  that takes shortcuts to simplify or improve performance. For example, a 
  fake data access object might return data from an in-memory datastore. 
  Mocks can mimic and simplify complex dependencies, but can also lead to 
  more mocks in order to replace nested dependencies.
- Testing with emulators: You can setup applications (sometimes from a 
  third party) to mimic a cloud service in your local environment. Speed is
  their strength, but setup and parity with production services is their 
  weakness. Use emulators sparingly.

Testing in the cloud
Test automation samples are available in 
https://github.com/aws-samples/serverless-test-samples

Although the test runs locally, it interacts with cloud-based resources. 
These resources have been deployed using the `AWS Serverless Application 
Model (SAM) and AWS SAM command line tool (which is not part os AWS CLI)`. 
The test code first retrieves the deployed stack outputs, which includes 
the API endpoint, function ARN, and security role. Next, the test sends a 
request to the API endpoint, which responds with a list of Amazon S3 
buckets. This test runs entirely against cloud-based resources to verify 
those resources are deployed, secured, and work as expected.
Unlike local testing, testing in the cloud requires additional resources 
which may incur service costs. Creating isolated testing environments may 
increase the burden on your DevOps teams, especially in organizations with 
strict controls around accounts and infrastructure.

Testing with mocks
Note that mock objects differ from emulators in that mocks are typically 
created or configured by a developer as part of the test code, whereas 
emulators are standalone applications that expose functionality in the same
manner as the systems they emulate.

Best Practices
- Structure your code for testability: Your Lambda function handler should 
  be a slim adapter that takes in event data and passes only the details 
  that matter to your business logic method(s). With this strategy, you can
  wrap comprehensive tests around your business logic without worrying 
  about Lambda-specific details. Your AWS Lambda functions should not 
  require setting up a complex environment or large amount of dependencies 
  to create and initialize the component under test.
  Generally speaking, you should write a handler that extracts and 
  validates data from the incoming event and context objects, then sends 
  that input to methods that perform your business logic.
- Prioritize testing in the cloud: Testing in the cloud provides the most 
  reliable, accurate, and complete test coverage. 
