# Creating an Amazon SNS topic
A topic is a logical access point that acts as a communication channel. A 
topic lets you group multiple endpoints (such as AWS Lambda, Amazon SQS, 
HTTP/S, or an email address).  
  
Use the AWS Management Console to create a topic.  
During creation, you choose a topic type (standard or FIFO) and name the 
topic. After creating a topic, you can't change the topic type or name. All
other configuration choices are optional during topic creation, and you can
edit them later.  

On the Create topic page, in the Details section, do the following:
1. For Type, choose a topic type (Standard or FIFO).  
2. Enter a Name for the topic. For a FIFO topic, add `.fifo` to the end of
   the name.

# Creating a subscription via AWS Management Console
Subscribing an endpoint to an Amazon SNS topic enables message delivery to
the specified endpoint, ensuring the right systems or users receive 
notifications when a message is published to the topic.  

1. In the left navigation pane, choose Subscriptions.
2. On the Subscriptions page, choose Create subscription.

