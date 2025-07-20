```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI( # there are many providers, you could use ollama provider.
    model="gpt-4o-mini",
    api_key="..."
) # instantiates a model from a given provider.

llm.invoke("What is LangChain?") # prompts the model.
```

## LangSmith
Deploying applications into production.
## LangGraph
Creating AI agents.
## Prompt Templates
Acts as a reusable recipe for defining prompts for LLMs.

Can contain: instructions, examples, and additional context that might help the model to complete the task.
```python
from langchain_core.prompts import PromptTemplate

# We can dynamically change the concept in this string.
example_template = "Explain this concept simply and concisely: {concept}"

# Converting the string into a prompt template
prompt_template = PromptTemplate.from_template(
	template=template
)

# To show how a variable will be inserted
prompt = prompt_template.invoke({"concept": "Prompting LLMs"})
print(prompt)
```
### Integrating prompt template and a model
```python
llm = HuggingFacePipeline.from_model_id(
	model_id="meta-llama/Llama3.3-70B-Instruct",
	task="text-generation"
)

llm_chain = prompt_template | llm # pipe operator

concept = "Prompting LLMs"

print(llm_chain.invoke({"concept": concept}))
```

The pipe operator is part of LangChain Expression Language (LCEL).
It's used to create a chain which connects a series of calls to different components into a sequence.

In the example above, the user input will be passed into the prompt template to populate it, then, the prompt will be inserted into the LLM.
## Prompt Roles
Each message in a model has a role:
- `system`: Used to define the model behavior.
- `human`: Provide user inputs.
- `ai`: Used for defining model responses, which is often used to provide additional examples for the model to learn from.

To create a prompt template including chat message roles, we'll use the `ChatPromptTemplate` class:
```python
from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages(
	[
		("system", "You are a calculator that responds with math."),
		("human", "Aswer this math question: What it two plus two?"),
		("ai", "2+2=4"),
		("human", "Answer this math question: {math}")
	]	
)
```

- `PromptTemplate` + `ChatPromptTemplate`: Are good for handling small number of examples.
- Don't scale for many examples.

`FewShotPromptTemplate` allows us to convert datasets into prompt templates to provide more context to the model.
```python
examples = [
	{
		{"question": "Does Henry Campbell have any pets?"},
		{"answer": "Henry Campbell has a dog called Pluto."}
	},
	...
]
```

Before we dive in with creating the few-shot prompt template, we need to decide how we want to structure the examples for the model.
```python
from langchain_core.prompts import FewShotTemplate, PromptTemplate

# Example of how questions and answers should be formatted.
example_prompt = PromptTemplate.from_template("Question: {question}\n{answer}")
```

To put everything together, few shot takes the examples list of dictionaries we created, and the template for formatting the examples.
Additionally, we can provide a suffix, which is used to format the user input, and specify what variable the user input will be assigned to.
```python
prompt_template = FewShotPromptTemplate(
	examples=examples,             # the list of dicts.
	example_prompt=example_prompt, # formatted template.
	suffix="Question: {input}",    # suffix to add to the input.
	input_variable=["input"]
)

llm = ChatOpenAI(...)

llm_chain = prompt_template | llm
response = llm_chain.invoke({"input": "What's the name of Henry Campbell's dog?"})
print(reponse.content)
```
## Sequential chains
In sequential chains, the output from one chain becomes the input to another.
```python
destination_prompt = PromptTemplate(
	input_variables=["destination"],
	template="I am planning a trip to {destination}. Can you suggest some activities to do there?"
)

activities_prompt = PromptTemplate(
	input_variables=["activities"],
	template="I only have one day, so can you create an intinerary from your top three activities: {activities}."
)

llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)

seq_chain = ({"activities": destination_prompt | llm | StrOutputParser()}) # passes the destination prompt to the llm and parses the output to string into the "activities" dictionary which is the input variable to the second prompt template.
	| activities_prompt # receives the first chain into the second prompt template.
	| llm #sends the activities prompt to the llm 
	| StrOutputParser() # converts the output into a string)

print(seq_chain.invoke({"destination": "Rome"}))
```
## LangChain Agents
To implement [agents](agents.md) we'll be using LangGraph which is a branch of LangChain centered around designing agent systems.

**ReAct agent example**
```python
from langgraph.prebuilt import create_react_agent
from langchain_community.agent_toolkits.load_tools import load_tools

llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)
tools = load_tools(["llm-math"], llm=llm) # loading llm-math tool.
agent = create_react_agent(llm, tools) # create the agent by passing the model and the available tools.

messages = agent.invoke({"messages": [{"human": "What is the square root of 101?"}]})
print(messages)
```
## Tools
In LangChain, tools must be formatted in a specific way to be compatible with agents.
1. They must have a name accessible via the .name attribute.
2. A description which is used by the LLM to determine when to call the tool.
3. a `return_direct` parameter indicates whether the agent should stop after invoking this tool.

```python
from langchain_core.tools import tool

@tool # marks the function as a valid tool for LangChain
def financial_report(company_name: str, revenue: int, expenses: int) -> str:
	"""Generate a financial report for a company that calculates net income."""
	net_income = revenue - expenses

	report = f"Financial Report for {company_name}:\n"
	report += f"Revenue: ${revenue}\n"
	report += f"Expenses: ${expenses}\n"
	report += f"Net Income: ${net_income}\n"
	return report

# we can add our tool in the list of tool for our agent
agent = create_react_agent(llm, [financial_report])
```