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
from langchain_core.output_parsers import StrOutputParser

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
To implement [agents](agents.md) we'll be using LangGraph which is a branch of LangChain centered around designing agentic systems.

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
## `RecursiveCharacterTextSplitter`
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
## RAG storage and retrieval using vector databases
We'll use a vector database to store our documents and make them available for retrieval.

This requires embedding our text documents to create vectors that capture the semantic meaning of the text.

Then, a user query can be embedded to retrieve the most similar documents from the database and insert them into the model prompt.

Vector database options:
![[Pasted image 20250721204530.png]]

When making the decision on which solution to choose, consider:
- Whether an open source solution is required, which may be the case if high customizability is required.
- Whether the data can be stored on off-premises on third-party servers - not all cases will permit this.
- The amount of storage and latency of retrieving results is also a key consideration.
## Example: using ChromaDB to create vector database
```python
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

embedding_function = OpenAIEmbeddings(
	api_key=openai_api_key,
	model="text-embedding-3-small"
)

vectorstore = Chroma.from_documents( # Creates a chroma database from a set of documents.
	docs,
	embedding=embedding_function,
	persist_directory="path/to/directory" # path were to store the database data
)

retriever = vectorstore.as_retriever( # enables integrating it with other LangChain components.
	search_type="similarity",
	search_kwargs={"k": 2} # returns the top two most similar documents for each user query.
)

# Building a prompt template
message = """
Review and fix the following TechStack marketing copy with the following guideline in consideration:

Guidelines:
{guidelines}

Copy:
{copy}

Fixed Copy:
"""

prompt_template = ChatPromptTemplate.from_messages([("human", message)])

# RunnablePassthrough acts as a placeholder to insert our input when we invoke the chain
rag_chain = ({"guidelines": retriever, "copy": RunnablePassthrough()}
			 | prompt_template
			 | llm)

response = rag_chain.invoke("Here at techstack, our users are the best in the world!")
```
## Loading and splitting code files
### Markdown
```python
from langchain_community.document_loaders import UnstructuredMarkdownLoader

loader = UnstructuredMarkdownLoader("README.md")
markdown_content = loader.load()
print(markdown_content[0])
```
### Python files
```python
from langchain_community.document_loaders import PythonLoader

loader = PythonLoader('chatbot.py')
python_data = loader.load()
print(python_data[0])
```
## Splitting complex files
### Code files
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

python_splitter = RecursiveCharacterTextSplitter.from_language(
	language=Language.PYTHON, # Argument that represents programming languages
	chunk_size=150,
	chunk_overlap=10
)

chunks = python_splitter.split_documents(data)
print(chunks[:3])
```

The `language` argument modifies the default separator list from the hierarchy of paragraphs, sentences and words `["\n\n", "\n", " ", ""]` to try splitting on classes and function definitions `["\nclass ", "\ndef ", "\n\tdef ", " ", ""]` before moving on to the standard separators

>As always you need to pay attention to your content and change `chunk_size` and `chunk_overlap` accordingly.
### Limitations of our current splitting strategies
The current approaches studied for splitting documents with character text splitters has the following limitations:
- Executed without considering the context of the surrounding text. This means that related information will potentially be stored and processed separately.
- Splits made using characters rather than tokens. Remember that the language models we're using, break text into tokens, or smaller units of text, for processing. By splitting documents using characters rather than tokens, we risk retrieving chunks and creating a retrieval prompt that exceed the maximum amount of text the model can process at once (model context window).

## Token Splitting
When we use a character text splitter with a `chunk_size` and `chunk_overlap`, we get chunks containing groups of characters that satisfy the chunking parameters.
When we split on tokens, the `chunk_size` and `chunk_overlap` refer to the number of tokens in the chunk, rather than characters, so a `chunk_size` of five means we can have a maximum of five tokens in the chunk.

![[Pasted image 20250722180646.png]]

```python
import tiktoken
from langchain_text_splitters import TokenTextSplitter


example_string = "Mary had a little lamb, it's fleece was white as snow."
encoding = tiktoken.encoding_for_model('gpt-4o-mini')
splitter = TokenTextSplitter(
	encoding_name=encoding.name, # encoding used by the llm
	chunk_size=10,
	chunk_overlap=2
)

chunks = splitter.split_text(example_string)
print(chunks)
```
## Semantic Splitting
A character or token text splitter will split naively, which results in lost context.

A semantic splitter will detect shifts in semantic meaning and perform the splits in those locations.
![[Pasted image 20250722181140.png]]

In this example, the text was splitted when the discussion shift from RAG to dogs.

To perform semantic splitting, we'll need an embedding model to generate text embeddings to determine the shift in topic.
```python
from langchain_openai import OpenAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker


embeddings = OpenAIEmbeddings(
	api_key="<OPENAI_API_KEY>",
	model="text-embedding-3-small"
)

semantic_splitter = SemanticChunker(
	embeddings=embeddings,
	breakpoint_threshold_type="gradient", # sets the metric at which embeddings are compared
	breakpoint_threshold_amount=0.8 # sets the mtetric's threshold at which to perform the split
)

chunks = semantic_splitter.split_documents(data)
print(chunks)
```
## Optimizing document retrieval
So far, our document retrieval has consisted of a vector database containing embedded documents. The input to the RAG application is then used to query the vectors, using a distance metric to determine which vectors are closest and therefore, most similar and relevant.

This type of retrieval is known as **dense retrieval**. Dense retrieval methods encode the entire chunk as a single vector that is said to be "dense", that is, most of its components values are non-zero.

Dense retrieval excels at capturing semantic meaning, but the embeddings can be computationally intensive to create and query, and may struggle with capturing rare words or highly specific technical terms.

There's also sparse retrieval, which is a method of finding information by matching specific keywords or terms in a query with those in documents. The resulting vectors contain many zeros, with only a few non-zero terms, which is why they are said to be "Sparse".

Sparse retrieval allows for precise retrieval, matching on exact words. The resulting vectors are also more explainable due to the alignment with specific terms, and rare words are better represented in the embeddings.

The trade-off is that Sparse retrieval methods are less generalizable, as they aren't extracting the semantic meaning from the text.
### Sparse retrieval methods
`TF-IDF` and `BM25` are the two popular methods for encoding text as spare vectors.

Term Frequency-Inverse Document (`TF-IDF`) creates a sparse vector that measures a term's frequency in a document and rarity in other documents. This helps in identifying words that best represent the document's unique content.
![[Pasted image 20250722183457.png]]

Best matching 25 (`BM25`) is an improvement on `TF_IDF` that prevents high-frequency words from being over-emphasized in the encoding.
```python
from langchain_core.output_parsers import StrOutputParser
from langchain_community.retrievers import BM25Retriever # Used to create a retriever from documents or text.

chunks = [
	"Python was created by Guido van Rossum and realeased in 1991.",
	"Python is a popular language for machine learning (ML).",
	"The PyTorch library is a popular Python library for AI and ML."
]

bm25_retriever = BM25Retriever.from_texts(
	chunks, 
	k=3 # Sets the number of items returned by the retriever when invoked.
)

results = bm25_retriever.invoke("When was Python created?")
print("Most Relevant Document:")
print(result[0].page_content)
```

Looking at all three statements again, we can see that `BM25` returned the statement with similar terms to the input that were also unique to the other statements.
### `BM25` in RAG

```python
retriever = BM25Retriever.from_documents(
	documents=chunks,
	k=5
)

chain = ({"context": retriever, "question": RunnablePassthrough()}
		 | prompt
		 | llm
		 | StrOutputParser()
)

print(chain.invoke("How can LLM hallucination impact a RAG application?"))
```
## RAG evaluation
Because our RAG architecture is made up of several processes, there are a few places where performance can be measured.

We can evaluate the:
- Retrieval process to check if the retrieved documents are relevant to the query.
- Generation process to see if the LLM hallucinated or misinterpreted the prompt
- Final output to measure the performance of the whole system.

![[Pasted image 20250722185231.png]]

We can use LLMs to measure the correctness of the final output by comparing it to a reference answer.

```python
from langchain.openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langsmith.evaluation import LangChainStringEvaluator


query = "What are the main components of RAG architecture?"
predicted_answer = "Traning and encoding"
ref_answer = "Retrieval and Generation"

prompt_template = """You are an expert professor specialized in grading student's answers.
You're grading the following question:{query}
Here is the real answer:{answer}
You are grading the following predicted answer:{result}
Repond with CORRECT or INCORRECT:
Grade:"""

prompt = PromptTemplate(
	input_variables=["query", "answer", "result"],
	template=prompt_template
)

eval_llm = ChatOpenAI(
	temperature=0, # set to 0 to minimize variability
	model="gpt-4o-mini",
	open_api_key="..."
)

# Output accuracy: string evaluation
# LangSmith is LangChain's platform for evaluating LLM applications.
qa_evaluator = LangChainStringEvaluator(
	"qa", # sets the evaluator to assess correctness
	config={
		"llm": eval_llm,
		"prompt": PROMPT
	}
)

score = qa_evaluator.evaluator.evaluate_strings(
	prediction=predicted_answer,
	reference=ref_answer,
	input=query
)

print(f"Score: {score}")
```

A score of zero indicates that predicted response was incorrect when compared to the reference answer.

To perform string evaluation, we need to define a prompt template and LLM to use for evaluation.
## Ragas framework
Designed to evaluate both the retrieval and generation components of a RAG application.

![[Pasted image 20250722190314.png]]
### Faithfulness
Assesses whether the generated output represents the retrieved documents well. It's calculated using LLM's to assess the ratio of faithful claims that can be derived from the context to the total number of claims.

![[Pasted image 20250722190449.png]]

Because faithfulness is a proportion, it is normalized to between zero and one, where a higher score indicates greater faithfulness.

Ragas integrates nicely with LangChain, and the first step involves defining the models for the evaluator to use:
- one for generation
- another for embeddings
```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from ragas.integrations.langchain import EvaluatorChain
from ragas.metrics import faithfulness

llm = ChatOpenAI(model="gpt-4o-mini", api_key="...")
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", api_key="...")

faithfulness_chain = EvaluatorChain(
	metric=faithfulness,
	llm=llm,
	embeddings=embeddings
)

# Evaluating faithfulness

eval_result = faithfulness_chain({
	# Question is the query sent to the RAG application
	"question": "How does the RAG model improve question answering with LLMs?",
	# Answer is the response
	"answer": "The RAG model improves question answering by combining the retrieval of documents...",
	# Context are the document chunks available to the model.
	"contexts": [
		"The RAG model integrates documents retrieval with LLMs by first retrieving relevant passages...",
		"By incorporating retrieval mechanisms, RAG leverages external knowledge sources, allowing the..."
	]	
})

print(eval_result)
```

Next, we define an evaluation chain, passing it the faithfulness metric from ragas and the two models we defined.
## Context precision
Measures how relevant the retrieved documents are to the query.

A context precision score closer to one means the retrieved context is highly relevant.

The only change we need to make to the faithfulness evaluation
```python
from ragas.metrics import faithfulness

llm = ChatOpenAI(model="gpt-4o-mini", api_key="...")
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", api_keys="...")


llm = ChatOpenAI(model="gpt-4o-mini", api_key="...")
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", api_key="...")

context_precision_chain = EvaluatorChain(
	metric=context_precision, # change made here
	llm=llm,
	embeddings=embeddings
)

# ...
eval_result = context_precision_chain({
	# Question is the query sent to the RAG application
	"question": "How does the RAG model improve question answering with LLMs?",
	# Ground Truth is used instead of "Answer" like in faithfulness, represnts the knowledge received from the context.
	"ground_truth": "The RAG model improves question answering by combining the retrieval of documents...",
	# Context are the document chunks available to the model.
	"context": [
		"The RAG model integrates documents retrieval with LLMs by first retrieving relevant passages...",
		"By incorporating retrieval mechanisms, RAG leverages external knowledge sources, allowing the..."
	]	
})

```
## From vectors to graphs
The RAG architecture we've explored involve embedding a user input and querying a vector store to return relevant documents based on their semantic similarity.
Although powerful, this approach does have some limitations:
1. Document embedding captures semantic meaning but struggles to capture themes and relationships between entities in the document corpus.
2. As the volume of the database grows, the retrieval process can become less efficient, as the computational load increases with the search space.
3. Vector RAG systems don't easily accommodate structured or diverse data, which are harder to embed.

All of those challenges can be addressed with graphs, which are great at representing and storing diverse and interconnected information in structured manner.

Objects are represented as nodes and relationships are represented by edges.
Notice that edges are directional, so relationships can apply from one entity to another, but not necessarily the other way around.

[Neo4j](https://neo4j.com/) is a powerful graph database option designed to store and efficiently query complex relationships.

We'll use LLMs to change unstructured text data into  a structured graph.
```python
from langchain_community.document_loaders import WikipediaLoader
from langchain_text_splitters import TokenTextSplitter
from langchain_openai import ChatOpenAI
from langchain_experimental.graph_transformers import LLMGraphTransformer

llm = ChatOpenAI(
	temperature=0, # produce more deterministic graphs for greathe reliability.
	...
)
llm_transformer = LLMGraphTransformer(llm=llm)

raw_documents = WikipediaLoader(query="large language model").load()
text_splitter = TokenTextSplitter(chunk_size=100, chunk_overlap=20)
documents = text_splitter.split_documents(raw_documents[:3])

print(documents[0])

graph_documents = llm_transformer.convert_to_graph_documents(documents)
print(graph_documents)
```
## Storing graphs for later querying
```python
from langchain_commuinty.graphs import Neo4jGraph

graph = Neo4jGraph(...) # provide connection options

graph.add_graph_documents(
	graph_documents, # from snippet above
	include_source=True, # links nodes to their source documents which as also represented as nodes, by including a MENTIONS relationship in the graph, enabling better traceability and context preservation.
	baseEntityLabel=True # assigns an additional __Entity__ label to each node, improving query perormance.
)

print(graph.get_schema) # return database schema, includes different node types and relationships, including their direction.

graph.refresh_schema() # refreshes current schema, good for auto-populated graphs.

# Neo4j uses Cypher Query language, which is a declarative query language for intuitively navigating and manipulating graph data using a SQL-like syntax.
results = graph.query("""
MATCH (gpt4:Model {id: "Gpt-4"})-[:DEVELOPED_BY]->(org:Organization)
RETURN org
""")

print(results)
```
## Building the Graph RAG architecture
- graph database: is populated with graph documents by using LLMs to infer the nodes and relationships.
- The application requires a user input, and that Cypher is required to query the Neo4j database and return the relevant documents.

The current missing part is how we're going to translate our user input into a Cypher query, analogous to how we embed user queries in vector RAG applications, and then return the graph result in natural language.

![[Pasted image 20250723185609.png]]

We'll be using LLMs to generate the Cypher query. For it to be able to generate the correct query we give it access to the graph schema containing the node properties and relationships.

The `GraphCypherQAChain` is really two sequential chains under the hood: a generate Cypher chain to generate the Cypher query, and a summarize results chain to return the natural language response.
![[Pasted image 20250723185922.png]]

```python
from langchain_comunity.chains.graph_qa.cypher import GraphCypherQAChain

# Performs translation from user input to cypher query based on graph schema.
# Also perform database lookup and converts graph result back to natual language.
chain = GraphCypherQAChain.from_llm(
	llm=ChatOpenAI(
		temperature=0,
		...
	),
	graph=graph,
	verbose=True # Allow Cypher query and resut returned from the database in the output.
) # not changing the default prompt templates for either of these steps:
# qa_prompt: prompt template for result generation
# cypher_prompt: Prompt template for Cypher generation
# cypher_llm: LLM for Cypher generation
# qa_llm: LLM for result generation

# It's possible to use different models for the two steps, and specify our own prompt templates using the arguements shown.

result = chain.invoke({"query": "What is the most accurate model?"})

print(f"Final answer: {result['result']}")
```
## Improving graph retrieval
The main limitation of using LLM to convert natural language to Cypher query is the non-deterministic nature of LLMs.

For large and complex graphs, LLMs can sometimes struggle to accurately infer the most relevant nodes and relationships to build the Cypher query. Quite often, you will only need the LLM to be aware of a subset of the graph, and excluding particular node types will not only make it easier for the LLM to accurately create the Cypher query, but it will improve the query latency.

Strategies to improve graph retrieval systems:
- Filtering Graph Schema
- Validating the Cypher Query
- Few-shot prompting
### Filtering
One way to improve the reliability or our Cypher queries is to filter down the search space:
```python
from langchain_community.chains.graph_qa.cypher import GraphCypherQAChain

llm = ChatOpenAI(temperature=0, ...)

# we can use exclude_types to specify nodes with given types to exclude from the database.
chain = GraphCypherQAChain.from_llm(
	graph=graph,
	llm=llm,
	exclude_types=["Concept"],
	verbose=True
)

print(graph.get_schema)
```

Removing unneeded node properties from the schema so the model can focus on a specific subset often improves the quality of the generated Cypher statements.
## Validating Cypher query
LLMs have particular difficulty with is inferring the direction of relationships when generating Cypher statements.

Because the graph schema is predefined when instantiating the chain, after the Cypher is generated, we can validate the query against the graph's schema.
```python
chain = GraphCypherQAChain.from_llm(
	...,
	validate_cypher=True # perform cypher validation and if necessary, correct the relationship directions in these generated statements.
)
```

Cypher validation:
- Detects Nodes and relationships.
- Determines the directions of the relationship.
- Checks the graph schema.
- Update the direction of relationships.
## Few-shot prompting
Provide the model with a few examples of user questions and their corresponding Cypher query.

Improves model performance on more complex queries and allows us to include more relevant examples for our use case.
```python
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

examples = [
	# list of dictionaries with "question" and "query" keys
]

example_prompt = PromptTemplate.from_template(
	"User input: {question}\nCypher query: {query}"
)

cypher_prompt = FewShotPromptTemplate(
	examples=examples,
	example_prompt=example_prompt,
	prefix="You are a Neo4j Expert ...",
	suffix="User input: {question}\nCypher query:",
	input_variables=["question"]
)

chain = GraphCypherQAChain.from_llm(
	graph=graph,
	llm=llm,
	cypher_prompt=cypher_prompt, # overrides default template
	verbose=True,
	validate_cypher=True
)
```
## Conversation history
```python
from langchain_core.messages import HumanMessage, AIMessage

# stores all of our messages
message_history = messages["messages"]

# New query, doesn't need to be appendend to the Chat template prompt bc we have the chat history.
new_query = "Some interesting query"

# Invokes the agent passing the whole conversation history
messages = app.invoke({"messages": message_history + [("human", new_query)]})

# Filter out only the relevant messages from the agent's response.
filtered_messages = [
	msg for msg in messages["messages"] 
	if isinstance(
		msg, 
		(HumanMessage, AIMessage) # Selcts both AI and Human messages
	) 
	and msg.content.strip()
]

#print response
```