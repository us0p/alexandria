# Chat history
Chat history is a record of the conversation between the user and the chat model. It is used to maintain context and state throughout the conversation.

The **assistant** may respond directly to the user or if configured with tools request that a tool be invoked to perform a specific task.

A full conversation often involves a combination of two patterns of alternating messages:
1. The **user** and the **assistant** representing a back-and-forth conversation.
2. The **assistant** and **tool messages** representing an "agentic" workflow where the assistant is invoking tools to perform specific tasks.
## Managing chat history
It's important to manage chat history and trim it as needed to avoid exceeding the [context window](langchain_chat_models.md#Context%20window).

While processing chat history, it's essential to preserve a correct conversation structure.

Key guidelines for managing chat history:
- The conversation should follow one of these structures:
    - The first message is either a "user" message or a "system" message, followed by a "user" and then an "assistant" message.
    - The last message should be either a "user" message or a "tool" message containing the result of a tool call.
- When using tool calling, a "tool" message should only follow an "assistant" message that requested the tool invocation.