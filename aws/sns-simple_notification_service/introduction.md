# Simple notification service (SNS)
Is a managed service that provides message delivery from publishers to 
subscribers (also known as producers and consumers).   
Publishers communicate asynchronously with subscribers by sending messages 
to a topic, which is a logical access point and communication channel.  
Clients can subscribe to the Amazon SNS topic and receive published 
messages using a supported endpoint type, such as Amazon Data Firehose, 
Amazon SQS, AWS Lambda, HTTP, email, mobile push notifications, and mobile
text messages (SMS).  

!["SNS services relation"](https://docs.aws.amazon.com/images/sns/latest/dg/images/sns-delivery-protocols.png)

[Official documentation](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)

## Features and capabilities
**Application-to-application messaging**: supports subscribers such as 
Amazon Data Firehose delivery streams, Lambda functions, Amazon SQS queues,
HTTP/S endpoints, and AWS Event Fork Pipelines. This allows for efficient 
message delivery in event-driven architectures.  
  
**Application-to-person notifications**: provide user notifications to 
subscribers such as mobile applications, mobile phone numbers, and email 
addresses.  
