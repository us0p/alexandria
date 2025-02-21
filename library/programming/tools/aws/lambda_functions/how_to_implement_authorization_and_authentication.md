How to implement authorization and authentication

Use a Lambda authorizer (formerly known as a custom authorizer) to control 
access to your API. When a client makes a request your API's method, API 
Gateway calls your Lambda authorizer. The Lambda authorizer takes the 
caller's identity as the input and returns an IAM policy as the output.
Use a Lambda authorizer to implement a custom authorization scheme. Your 
scheme can use request parameters to determine the caller's identity or use
a bearer token authentication strategy such as OAuth or SAML. Create a 
Lambda authorizer in the API Gateway REST API console, using the AWS CLI, 
or an AWS SDK.

API Gateway Lambda authorization workflow
- The client calls a method on an API Gateway API, passing a bearer token 
  or request parameters.
- API Gateway checks if the method request is configured with a Lambda 
  authorizer. If it is, API Gateway calls the Lambda function.
- The Lambda function authenticates the caller. The function can 
  authenticate in the following ways:
    - By calling out to an OAuth provider to get an OAuth access token.
    - By calling out to a SAML provider to get a SAML assertion.
    - By generating an IAM policy based on the request parameter values.
    - By retrieving credentials from a database.
- The Lambda function returns an IAM policy and a principal identifier. If 
  the Lambda function does not return that information, the call fails.
- API Gateway evaluates the IAM policy.
    - If access is denied, API Gateway returns a suitable HTTP status 
      code, such as 403 ACCESS_DENIED.
    - If access is allowed, API Gateway invokes the method.
    - If you enable authorization caching, API Gateway caches the policy so
      that the Lambda authorizer function isn't invoked again.

Choosing a type of lambda authorizer:
- Request parameter-based Lambda authorizer (REQUEST authorizer): A REQUEST
  authorizer receives the caller's identity in a combination of headers, 
  query string parameters, stageVariables, and $context variables. You can 
  use a REQUEST authorizer to create fine-grained policies based on the 
  information from multiple identity sources, such as the $context.path and
  $context.httpMethod context variables.
- Token-based Lambda authorizer (TOKEN authorizer): A TOKEN authorizer 
  receives the caller's identity in a bearer token, such as a JSON Web 
  Token (JWT) or an OAuth token.
