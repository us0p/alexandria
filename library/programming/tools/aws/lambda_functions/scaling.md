# Function Scaling
Concurrency is the number of in-flight requests that your AWS Lambda 
function is handling at the same time. For each concurrent request, Lambda
provisions a separate instance of your execution environment. As your 
functions receive more requests, Lambda automatically handles scaling the 
number of execution environments until you reach your account's concurrency
limit. By default, Lambda provides your account with a total concurrency 
limit of `1,000 concurrent executions across all functions in an AWS 
Region`.
To support your specific account needs, you can request a quota increase 
and configure function-level concurrency controls so that your critical 
functions don't experience throttling.

## Understanding concurrency
Lambda invokes your function in a secure and isolated execution 
environment. To handle a request, Lambda must first initialize an execution
environment (the Init phase), before using it to invoke your function 
(the Invoke phase).
When your function receives its very first request, Lambda creates a new 
execution environment and runs the init and invoke phases.
During this entire process, this execution environment is busy and cannot 
process other requests.
When Lambda finishes processing the first request, this execution 
environment can then process additional requests for the same function. For
subsequent requests, Lambda doesn't need to re-initialize the environment.
In practice, Lambda may need to provision multiple execution environment 
instances in parallel to handle all incoming requests. When your function 
receives a new request, one of two things can happen:
- If a pre-initialized execution environment instance is available, Lambda
  uses it to process the request.
- Otherwise, Lambda creates a new execution environment instance to process
  the request.
To summarize, your function's concurrency is the number of concurrent 
requests that it's handling at the same time. In response to an increase in
your function's concurrency, Lambda provisions more execution environment 
instances to meet request demand.

## Calculating concurrency for a function
`C = (avg req p/ second) * (avg req duration in seconds)`
What does a concurrency of 50 mean in practice? If the average request 
duration is 500 ms, then you can think of an instance of your function as 
being able to handle two requests per second. Then, it takes 50 instances 
of your function to handle a load of 100 requests per second. A concurrency
of 50 means that Lambda must provision 50 execution environment instances 
to efficiently handle this workload without any throttling.

## Understanding reserved concurrency and provisioned concurrency
By default, your account has a concurrency limit of `1,000 concurrent 
executions across all functions in a Region`. Your functions share this 
pool of 1,000 concurrency on an on-demand basis. Your functions experiences 
throttling (that is, they start to drop requests) if you run out of 
available concurrency.
Some of your functions might be more critical than others. As a result, you
might want to configure concurrency settings to ensure that critical 
functions get the concurrency that they need. There are two types of 
concurrency controls available:
- Reserved concurrency: reserve a portion of your account's concurrency for
  a function. This is useful if you don't want other functions taking up 
  all the available unreserved concurrency.
- Use provisioned concurrency: pre-initialize a number of environment 
  instances for a function. This is useful for reducing cold start 
  latencies.
Reserved concurrency is the maximum number of concurrent instances that you
want to allocate to your function. When you dedicate reserved concurrency 
to a function, no other function can use that concurrency.
If a function with reserved concurrency hits the max concurrency, even if
there's unused concurrency elsewhere, the function cannot access it, thus
the function starts to experience throttling and lambda may drop requests.
The same is valid for functions with withour reserved concurrency, if the
available concurrency pool is consumed, they might experience throttling
and Lambda may drop requests.
Note that none of the environments provided by reserved concurrency come 
pre-initialized. As a result, your function invocations may take longer 
because Lambda must first initialize the new environment before being able
to use it to invoke your function.
This is known as a cold start. To mitigate cold starts, you can use 
provisioned concurrency.
Using provisioned concurrency incurs additional charges to your account.
When using provisioned concurrency, Lambda still recycles execution 
environments in the background. However, at any given time, Lambda always 
ensures that the number of pre-initialized environments is equal to the 
value of your function's provisioned concurrency setting. This behavior 
differs from reserved concurrency, where Lambda may completely terminate an
environment after a period of inactivity.
Functions with provisioned concurrency can use unreserved concurrency if it
hits the provisioned concurrency limit (there's no throttling), lambda 
must create new instances to serve these requests, and your function may 
experience cold start latencies.
However, functions that have to use the unreserved concurrency may still
experience throttling if they reach the limit of the unreserved 
concurrency.
In practice, you can set both provisioned concurrency and reserved 
concurrency on a function.
Configuring provisioned concurrency incurs charges to your AWS account.

Understanding concurrency and requests per second
As mentioned in the previous section, concurrency differs from requests per
second. This is an especially important distinction to make when working 
with functions that have an average request duration of less than 100 ms.
Across all functions in your account, Lambda enforces a requests per second
limit that's equal to 10 times your account concurrency. For example, since
the default account concurrency limit is 1,000, functions in your account 
can handle a maximum of 10,000 requests per second.
For example, consider a function with an average request duration of 50 ms.
At 20,000 requests per second, here's the concurrency of this function:

C = 20_000 p/ second * 0.05 (50ms) duration p/ request = 1_000

Based on this result, you might expect that the account concurrency limit 
of 1,000 is sufficient to handle this load. However, because of the 10,000 
requests per second limit, your function can only handle 10,000 requests 
per second out of the 20,000 total requests. This function experiences 
throttling.
The lesson is that you must consider both concurrency and requests per 
second when configuring concurrency settings for your functions. In this 
case, you need to request an account concurrency lmiit increase to 2,000, 
since this would increase your total requests per second limit to 20,000.
Based on this request per second limit, it's incorrect to say that each 
Lambda execution environment can handle only a maximum of 10 requests per 
second.
