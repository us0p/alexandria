# Messages
Unit of communication in chat models. Used to represent the input and output of a chat model, as well as any additional context or metadata associated with a conversation.

Each message has a **role** and **content** with additional metadata that varies depending on the chat model provider.

Roles can be:
- **System**: Used to tell the chat model how to behave and provide additional context.
- **User**: Represents input from an user interacting with the model.
- **Assistant**: Represents the response from the model.
- **Tool**: A message used to pass the results of a tool invocation back to the model after external data or processing has been retrieved.