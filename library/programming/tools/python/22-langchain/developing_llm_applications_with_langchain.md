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
## RAG
Use embeddings to retrieve relevant information to integrate into the prompt.

There are three primary steps to RAG development in LangChain:
1. Loading the document into LangChain with document loaders.
2. Splitting the documents into chunks (units of information we can index and process individually), particularly useful for breaking up long documents so that they fit within a LLM's context window.
3. Encoding and storing the chunks for retrieval, which could utilize a vector database.

LangChain document loaders are classes designed to load and configure documents for system integration.
LangChain provide document loaders for common file types:
- `.pdf`
- `.csv`

There are also 3rd party loaders that can provide support for many other files as well.
### PDF document loader
```python
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("path/to/file")

data = loader.load() # loads the document into memory
```
### CSV document loader
```python
from langchain_community.document_loaders.csv_loader import CSVLoader

loader = CSVLoader("file.csv")

data = loader.load()
```
### HTML document loader
```python
from langchain_community.document_loaders import UnstructuredHTMLLoader

loader = UnstructuredHTMLLoader("file.html")
data = loader.load()
```
## Splitting
There isn't one document splitting strategy that works for all situations. We should experiment with multiple methods, and see which one strikes the right balance between retaining context and managing chunk size.

For example, splitting a document line by line is simple, but since sentences are often split over multiple lines, and because those lines are processed separately, key context might be lost. 
To counteract lost context during chunk splitting, a chunk overlap is often implemented. In this, between two chunks, there's an overlap which is replicated in both chunks to help keep context.
![[Pasted image 20250720092927.png]]

If a model shows signs of losing context and misunderstanding information when answering from external sources, you may need to increase this chunk overlap.

We will compare two document splitting methods:
- `CharacterTextSplitter`
- `RecursiveCharacterTextSplitter`

>Optimizing this document splitting is an active area of research, so keep an eye out for new developments!
## `CharacterTextSplitter`
Splits on the separator first, then evaluates `chunk_size` and `chunk_overlap` to check if it's satisfied.
```python
from langchain_text_splitters import CharacterTextSplitter

ct_splitter = CharacterSplitter(
	separator='.',
	chunk_size=chunk_size,
	chunk_overlap=chunk_overlap
)

docs = ct_splitter.split_text(quote)
```

It tries to split on the separator so < `chunk_size`, but may not always succeed.
## `RecursiveCharacterSplitter`
Takes a list of separators to split on, and it works through the list from left to right, splitting the document using each separator in turn, and seeing if these chunks can be combined while remaining under `chunk_size`.
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

rc_splitter = RecursiveCharacterTextSplitter(
	separators=["\n\n", "\n", " ", ""],
	chunk_size=chunk_size,
	chunk_overlap=chunk_overlap
)

docs = rc_splitter.split_text(quote)
```
## `RecursiveCharacterTextSplitter` with HTML

```python
from langchain_community.document_loaders import UnstructuredHTMLLoader

loader = UnstructuredHTMLLoader("white_house_execution_order_nov_2023.html")
data = loader.load()

rc_splitter = RecursiveCharacterTextSplitter(
	chunk_size=chunk_size,
	chunk_overlap=chunk_overlap,
	separators=['.']
)

docs = rc_splitter.split_documents(data)
```