# AWS Lambda
Is an event-driven compute service that runs instances of your functions to
process events. You can invoke your function directly using the Lambda API,
or you can configure an AWS service or resource to invoke your function.
It's a serverless compute service that automatically manages the underlying
compute resources for you.

AWS Lambda automatically monitors Lambda functions and reports metrics 
through Amazon CloudWatch. To help you monitor your code as it executes, 
Lambda automatically tracks the number of requests, the latency per 
request, and the number of requests resulting in an error and publishes the
associated metrics.

## AWS Step Functions
Step Functions is a serverless orchestration service that lets you easily 
coordinate multiple Lambda functions into flexible workflows that are easy 
to debug and change. Step Functions will keep your Lambda functions free of
additional logic by triggering and tracking each step of your application 
for you.
Step Functions uses Amazon States Language (ASL) a JSON-based, structured 
language to define state machines.
This language is used to define the workflow of your state machine and to
bind lambda functions to each step in your workflow.

## Lambda key concepts
Function
Is a resource that you can invoke to run your code in lambda. A function
has code to process the events that you pass into the function or that
other AWS services send to the function.

Trigger
Is a resource or configuration that invokes a lambda function. Triggers
include AWS services that you can configure to invoke a function and
event source mappings which is a resource in lambda that reads items from
a stream or queue and invokes a function.

Event
Is a JSON-formatted document that contains data for a Lambda function to 
process. The runtime converts the event to an object and passes it to your 
function code.
When you invoke a function, you determine the structure and contents of the
event.
When an AWS service invokes your function, the service defines the shape of
the event (each service has a specific format).

Execution Environment
An execution environment provides a secure and isolated runtime environment
for your Lambda function. An execution environment manages the processes 
and resources that are required to run the function. The execution 
environment provides lifecycle support for the function and for any 
extensions associated with your function.

Deployment package
You deploy your Lambda function code using a deployment package. Lambda 
supports two types of deployment packages:
- A .zip file archive that contains your function code and its 
  dependencies. Lambda provides the operating system and runtime for your 
  function.
- A container image that is compatible with the OCI specification. You add 
  your function code and dependencies to the image. You must also include 
  the operating system and a Lambda runtime.

Runtime
The runtime provides a language-specific environment that runs in an 
execution environment. The runtime relays invocation events, context 
information, and responses between Lambda and the function. You can use 
runtimes that Lambda provides, or build your own.

Layer
A Lambda layer is a .zip file archive that can contain additional code or 
other content. A layer can contain libraries, a custom runtime, data, or 
configuration files.
Using layers reduces the size of uploaded deployment archives. Layers also 
promote code sharing and separation of responsibilities.
You can include up to five layers per function. When you include a layer in
a function, the contents are extracted to the /opt directory in the 
execution environment.
Functions deployed as a container image do not use layers. Instead, you 
package your preferred runtime, libraries, and other dependencies into the 
container image when you build the image.

Concurrency
Concurrency is the number of requests that your function is serving at any 
given time. When your function is invoked, Lambda provisions an instance of
it to process the event. When the function code finishes running, it can 
handle another request. If the function is invoked again while a request is
still being processed, another instance is provisioned, increasing the 
function's concurrency.

Qualifier
When you invoke or view a function, you can include a qualifier to specify 
a version or alias. A version is an immutable snapshot of a function's code
and configuration that has a numerical qualifier. For example, 
my-function:1. An alias is a pointer to a version that you can update to 
map to a different version, or split traffic between two versions. For 
example, my-function:BLUE. You can use versions and aliases together to 
provide a stable interface for clients to invoke your function.

Destination
A destination is an AWS resource where Lambda can send events from an 
asynchronous invocation. You can configure a destination for events that 
fail processing. Some services also support a destination for events that 
are successfully processed.
