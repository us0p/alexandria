# Tools
A way to encapsulate a function and its schema in a way that can be passed to a chat model.

The key attributes that correspond to the tool's schema:
- **name**: The name of the tool.
- **description**: A description of what the tool does.
- **args**: Property that returns the JSON schema for the tool's arguments.

Tools can be passed to [chat models](langchain_chat_models.md) that support tool calling.
## Tools artifacts
**Tools** are utilities that can be called by a model, and whose outputs are designed to be fed back to a model. Sometimes, however, there are artifacts of a tool's execution that we want to make accessible to downstream components in our chain or agent, but that we don't want to expose to the model itself.
## Special type annotations
There are a number of special type annotations that can be used in the tool's function signature to configure the run time behavior of the tool.

The following type annotations will end up **removing** the argument from the tool's schema. This can be useful for arguments that should not be exposed to the model and that the model should not be able to control.

- `InjectedToolArg`: Value should be injected manually at runtime using `.invoke` or `.ainvoke`.
- `RunnableConfig`: Pass in the `RunnableConfig` object to the tool.
- `InjectedState`: Pass in the overall state of the [LangGraph](langgraph.md) graph to the tool.
- `InjectedStore`: Pass in the [LangGraph](langgraph.md) store object to the tool.

You can also use the `Annotated` type with a string literal to provide a **description** for the corresponding argument that **WILL** be exposed in the tool's schema.
```python
# Adds a description to the argument that will be exposed in the tool's schema.
Annotated[..., "string literal"] 
```
## Toolkits
Abstraction that groups tools together that are designed to be used together for specific tasks.

All toolkits expose a `get_tools` method which returns a list of tools.
## Best practices
- Tools that are well-named, correctly-documented and properly type-hinted are easier for models to use.
- Design simple and narrowly scoped tools, as they are easier for models to use correctly.
- Use chat models that support tool-calling API to take advantage of tools.
- Asking the model to select from a large list of tools poses challenges for the model.