# Memory
## Short-term memory
Also known as thread-scoped memory, tracks the ongoing conversation by maintaining message history within a session.

[LangGraph](langgraph.md) manages short-ter memory as part of your agent's state.

State is persisted to a database using a `checkpointer` so the thread can be resumed at any time.

Short-term memory updates when the graph is invoked or a step is completed, and the State is read at the start of each step.
## Manage short-term memory
In chat applications, messages alternate between human inputs and model responses, resulting in a list of messages that grows longer over time. Because context windows are limited, many applications can benefit from using techniques to manually remove or forget stale information.

![[Pasted image 20250728192801.png]]
## Long-term memory
Stores user-specific or application-level data across sessions and is shared across conversational threads. It can be recalled at any time and in any thread.

Memories are scoped to any custom namespace, not just within a single thread ID.

[LangGraph](langgraph.md) provides **stores** to let you save and recall long-term memories.

![[Pasted image 20250728192348.png]]

Long-term memory is a complex challenge without a one-size-fits-all solution. However, the following questions provide a framework to help you navigate the different techniques:

- What is the type of memory? Humans use memories to remember facts (semantic memory), experiences (episodic memory), and rules (procedural memory). AI agents can use memory in the same ways.
- When do you want to update memories? Memory can be updated as part of an agent's application logic. In this case, the agent typically decides to remember facts before responding to a user. Alternatively, memory can be updated as a background task.

## Memory types
Examining [human memory types](https://www.psychologytoday.com/us/basics/memory/types-of-memory?ref=blog.langchain.dev) can be insightful.

| Memory Type                                                                                                                                                                                                                                       | What is Stored | Human Example              | Agent Example       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | -------------------------- | ------------------- |
| [Semantic](https://langchain-ai.github.io/langgraph/concepts/memory/?_gl=1*1i4a70r*_gcl_au*MTM1NDY5MDQzNy4xNzUyMjk1MzA5*_ga*MjA0MjQ0NjkwNy4xNzUzNjk3NDg5*_ga_47WX3HKKY2*czE3NTM2OTc0ODgkbzEkZzEkdDE3NTM2OTgzNzEkajM4JGwwJGgw#semantic-memory)     | Facts          | Things I learned in school | Facts about a user  |
| [Episodic](https://langchain-ai.github.io/langgraph/concepts/memory/?_gl=1*1i4a70r*_gcl_au*MTM1NDY5MDQzNy4xNzUyMjk1MzA5*_ga*MjA0MjQ0NjkwNy4xNzUzNjk3NDg5*_ga_47WX3HKKY2*czE3NTM2OTc0ODgkbzEkZzEkdDE3NTM2OTgzNzEkajM4JGwwJGgw#episodic-memory)     | Experiences    | Things I did               | Past agent actions  |
| [Procedural](https://langchain-ai.github.io/langgraph/concepts/memory/?_gl=1*1i4a70r*_gcl_au*MTM1NDY5MDQzNy4xNzUyMjk1MzA5*_ga*MjA0MjQ0NjkwNy4xNzUzNjk3NDg5*_ga_47WX3HKKY2*czE3NTM2OTc0ODgkbzEkZzEkdDE3NTM2OTgzNzEkajM4JGwwJGgw#procedural-memory) | Instructions   | Instincts or motor skills  | Agent system prompt |
## Writing memories
### In the hot path
This approach allows for real-time updates, making new memories immediately available for use in subsequent interactions. It also enables transparency, as users can be notified when memories are created and stored.

However, It may increase complexity if the agent requires a new tool to decide what to commit to memory. In addition, the process of reasoning about what to save to memory can impact agent latency.

Finally, the agent must multitask between memory creation and its other responsibilities, potentially affecting the quantity and quality of memories created.
### In the background
It eliminates latency in the primary application, separates application logic from memory management, and allows for more focused task completion by the agent. This approach also provides flexibility in timing memory creation to avoid redundant work.

However, this method has its own challenges. Determining the frequency of memory writing becomes crucial, as infrequent updates may leave other threads without new context. Deciding when to trigger memory formation is also important.
## Memory Storage
LangGraph stores long-term memories as JSON documents in a [store](https://langchain-ai.github.io/langgraph/concepts/persistence/#memory-store).

Each memory is organized under a custom `namespace` (similar to a folder) and a distinct `key` (like a file name).

Namespaces often include user or org IDs or other labels that makes it easier to organize information. This structure enables hierarchical organization of memories.

Cross-namespace searching is then supported through content filters.