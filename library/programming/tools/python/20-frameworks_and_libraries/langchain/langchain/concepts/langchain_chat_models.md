# Chat models
LangChain provides a chat model interface that takes a list of messages as input and returns message as output.

**Some** chat models supports additional capabilities, such as:
- **Tool calling**: Allow tool calls to perform tasks such as fetching data from a database, making API requests, or running custom code.
- **Structured output**: Allows models to be requested to respond into a particular format (e.g. JSON matching a particular schema).
- **Multimodality**: For models capable of processing other types of data such as image, audio, and video.
## Context Window
Maximum size of the input sequence the model can process at one time.

Even if your LLM supports the full context length, most LLMs still perform poorly over long contexts. They get "distracted" by stale or off-topic content, all while suffering from slower response times and higher costs.