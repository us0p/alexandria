# Structured Outputs
Models can be instructed to respond with a particular output structure.

- **Schema definition**: The output structure is represented as a schema, which can be defined in several ways.
- **Returning structured output**: The model is given this schema, and is instructed to return output that conforms to it.
## Returning structured output
With a schema defined, we need a way to instruct the model to use it.
## Using [tool calling](langchain_tools.md)
We can simply bind our schema to a model as a tool.
## JSON mode
This supports JSON schema definition as input and enforces the model to produce a conforming JSON output.
## Structured output method
There are a few challenges when producing structured output with the above methods:
1. When tool calling is used, tool call arguments needs to be parsed from a dictionary back to the original schema.  
2. In addition, the model needs to be instructed to _always_ use the tool when we want to enforce structured output, which is a provider specific setting.  
3. When JSON mode is used, the output needs to be parsed into a JSON object.

With these challenges in mind, LangChain provides a helper function (`with_structured_output()`) to streamline the process.