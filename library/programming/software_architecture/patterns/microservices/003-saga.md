# Saga
You have applied the Database per Service pattern. Each service has its own
database. Some business transactions, however, span multiple service so you
need a mechanism to implement transactions that span services.

Problem
How to implement transactions that span services in a distributed database
architecture?

Solution
Implement each business transaction that spans multiple services as a saga.
A saga is a sequence of local transactions.
Each local transaction updates the database and publishes a message or 
event to trigger the next transaction in the saga.
If a local transaction fails *because it violates a business rule* then the 
saga executes a series of compensating transactions that undo the changes 
that were made by the preceding local transactions.

There are two ways of coordinating sagas:
- Choreography: each local transaction publishes domain events that trigger
  local transactions in other services.
- Orchestration: an orchestrator (object) tells the participants what local
  transactions to execute.

Benefits
- It enables an application to maintain data consistency across multiple 
  services without using distributed transactions.

Drawbacks
- Lack of automatic rollback: a developer must design compensating 
  transactions that explicitly undo changes made earlier in a saga rather 
  than relying on the automatic rollback feature of ACID transactions.
- Lack of isolation: the lack of isolation means that there’s risk that the
  concurrent execution of multiple sagas and transactions can use data 
  anomalies. consequently, a saga developer must typical use 
  countermeasures, which are design techniques that implement isolation.

Issues to address at implementation
- In order to be reliable, a service must atomically update its database 
  and publish a message/event. It cannot use the traditional mechanism of a
  distributed transaction that spans the database and the message broker. 
  Instead, it must use one of the patterns listed below.
- A client that initiates the saga, which an asynchronous flow, using a 
  synchronous request (e.g. HTTP POST /orders) needs to be able to 
  determine its outcome. There are several options, each with different 
  trade-offs:
    - The service sends back a response once the saga completes, e.g. once 
      it receives an OrderApproved or OrderRejected event.
    - The service sends back a response (e.g. containing the orderID) after
      initiating the saga and the client periodically polls (e.g. GET 
      /orders/{orderID}) to determine the outcome
    - The service sends back a response (e.g. containing the orderID) after
      initiating the saga, and then sends an event (e.g. websocket, web 
      hook, etc) to the client once the saga completes.
