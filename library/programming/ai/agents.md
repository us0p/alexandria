# What is an Agent
AI model capable of reasoning, planning, and interacting (execution of actions, often via external tools) with its environment.
We call it Agent because it has agency, the ability to interact with the environment.

Planning is the step in which the LLM decide the sequence of actions and select appropriate tools needed to fulfill the user's request.
Tools provide the Agent with the ability to execute actions a text-generation model cannot perform natively, such as generating images.

Agents have two main parts:
1. The brain (AI Model): Handles reasoning and planning, deciding which actions to take based on the situation. It understands and interpretes natural language, analyze information, make decisions, and strategies to solve problems.
2. The Body (Tools): Everything the Agent is equipped to do. The scope of possible actions depends on what the agent has been equipped with. It uses the tools to interact with the environment to, for example, gather information, take actions, and observe the result of those actions.

The most common AI model found in Agents are LLMs (Large Language Model). But it's also possible to use models that accept other inputs as the Agent's core model. For example VLM (Vision Language Model) which also understands images as input.

An Agent can perform any task we implement via Tools to complete Actions.
The design of the Tools is very important and has a great impact on the quality of your Agent.

>Note that Actions are not the same as Tools. An Action, for instance, can involve the use of multiple Tools to complete.
>Actions are the steps the Agent takes, while Tools are external resources the Agent can use to perform those Actions.
## Examples
1. Personal virtual assistants: Take user queries, analyze context, retrieve information from databases, and provide responses or initiate actions.
2. Customer service chatbots: Can answer questions, guide users through troubleshooting steps, open issues in internal databases, or even complete transactions.
3. AI Non-Playable Character in games: Can respond contextually, adapt to player interactions, and generate more nuanced dialogue.
# What are LLMs?
Is a type of AI model that excels at understanding and generating human language. They are trained on vast amounts of text data, allowing them to learn patterns, structure, and even nuance in language.

Most LLMs nowadays are built on the Transformer architecture, a deep learning architecture based on the "Attention" algorithm.
There are 3 types of transformers:
### Encoders
Takes text (or other data) as input and outputs a dense representation (or embedding) of that text.
- **Example**: BERT from Google
- **Use Cases**: Text classification, semantic search, Named Entity Recognition
- **Typical Size**: Millions of parameters
### Decoders
Focuses on generating new tokens to complete a sequence, one token at a time.
- **Example**: Llama from Meta
- **Use Cases**: Text generation, chatbots, code generation
- **Typical Size**: Billions of parameters
### Seq2Seq (Encoder-Decoder)
Combines an encoder and a decoder. The encoder first processes the input sequence into a context representation, then the decoder generates an output sequence.
- **Example:** T5, BART
- **Use Cases**: Translation, Summarization, Paraphrasing
- **Typical Size**: Millions of parameters

Although LLMs come in various forms, LLMs are typically decoder-based models with billions of parameters.

The underlying principle of an LLM is to predict the next token, given a sequence of previous token. A "token" is the unit of information an LLM works with. You can think of a "token" as if it was a "word", but for efficiency reasons LLMs don't use whole words.

For example, while English has an estimated 600,000 words, an LLM might have a vocabulary of around 32,000 tokens (as is the case with Llama 2). Tokenization often works on sub-word units that can be combined.

For instance, consider how the tokens “interest” and “ing” can be combined to form “interesting”, or “ed” can be appended to form “interested.”

Each LLM has some **special tokens** specific to the model. The LLM use these tokens to open and close the structured components of its generation. Moreover, the input prompts that we pass to the model are also structured with special tokens. The most important is the **end of sequence token** (EOS).

| **Model**       | **Provider**                | **EOS Token**           | **Functionality**             |
| --------------- | --------------------------- | ----------------------- | ----------------------------- |
| **GPT4**        | OpenAI                      | `<\|endoftext\|>`       | End of message text           |
| **Llama 3**     | Meta (Facebook AI Research) | `<\|eot_id\|>`          | End of sequence               |
| **Deepseek-R1** | DeepSeek                    | `<\|end_of_sentence\|>` | End of message text           |
| **SmolLM2**     | Hugging Face                | `<\|im_end\|>`          | End of instruction or message |
| **Gemma**       | Google                      | `<end_of_turn>`         | End of conversation turn      |
You shouldn't memory all the tokens, but you should appreciate their diversity and the role they play in the text generation of LLMs.
## Understanding next token prediction
LLMs are said to be **autoregressive**, meaning that **the output from one pass becomes the input for the next one**. This loop continues until the model predicts the next token to be the EOS token.

[Example token prediction example](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit1/AutoregressionSchema.gif)

But what happens during a single decoding loop?
- Once the input text is **tokenized**, the model computes a representation of the sequence that captures information about the meaning and the position of each token in the input sequence.
- This representation goes into the model, which outputs scores that rank the likelihood of each token in its vocabulary as being the next one in the sequence. 

[Example of single decoding loop prediction](https://cdn-lfs-us-1.hf.co/repos/45/f4/45f48d5b3577034b76ee728dfe60afca3d0aa70790fda3e706eeb9276d8d5331/51160fb55461970933039680c9a5ab21a35d0b42f3383ab2bd52a47d63fcb40d?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27DecodingFinal.gif%3B+filename%3D%22DecodingFinal.gif%22%3B&response-content-type=image%2Fgif&Expires=1742942814&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0Mjk0MjgxNH19LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy11cy0xLmhmLmNvL3JlcG9zLzQ1L2Y0LzQ1ZjQ4ZDViMzU3NzAzNGI3NmVlNzI4ZGZlNjBhZmNhM2QwYWE3MDc5MGZkYTNlNzA2ZWViOTI3NmQ4ZDUzMzEvNTExNjBmYjU1NDYxOTcwOTMzMDM5NjgwYzlhNWFiMjFhMzVkMGI0MmYzMzgzYWIyYmQ1MmE0N2Q2M2ZjYjQwZD9yZXNwb25zZS1jb250ZW50LWRpc3Bvc2l0aW9uPSomcmVzcG9uc2UtY29udGVudC10eXBlPSoifV19&Signature=pxDGWZAqqfx7uDG0IcgRFtrUwpZzx0jAyTuGlJdRsk5VXvZCaes97wEVrkTJw3Y8sqfUDhrq53qw6XpShMrHiuj96ww3JIv6dGBmdOWGuOMOO3YDo05hoh1jjQPvBKC8xBuEnjVVbmdQKKosj3IhGIlwE%7EMzNSJUeTcTqbpauLSl2qbEPECjoLlilYMObdPLF8PaU23VE%7ENXH3Ly%7EXhjzFpLZZfZAeQoY9YqGuFIW1SYmtHAFsz2Jk2f9l0wgqtAyXL%7EMU5QGJ7QkXR1HR2dfMlpwBsqej46QdCS1qAenLbStRazarPP0iUFdpfyiYHJ0o3s8WwkHZgdI4jrdRAUnw__&Key-Pair-Id=K24J24Z295AEI9)

Based on these scores, we have multiple strategies to select the tokens to complete the sentence.
The easiest decoding strategy would be to always take the token with the maximum score.
But there are some advanced decoding strategies. For example, **beam search**. It explores multiple candidate sequences to find the one with the maximum total score, even if some individual tokens have lower scores.
## Attention is all you need
A key aspect of the Transformer architecture is Attention. When predicting the next word, not every word in a sentence is equally important, words like "France" and "capital" in the sentence "The capital of France is ..." carry the most meaning.

This process of identifying the most relevant words to predict the next token has proven to be incredibly effective.
## Prompting the LLM is important
The input sequence you provide an LLM is called a *prompt*. Careful design of the prompt makes it easier to guide the generation of the LLM toward the desired output.
Considering that the only job of an LLM is to predict the next token by looking at every input token, and to choose which tokens are "important".
## How are LLMs trained
LLMs are trained on large datasets of text, where they learn to predict the next word in a sequence through a self-supervised or masked language modeling objective.

From this unsupervised learning, the model learns the structure of the language and **underlying patterns in text, allowing the model to generalize to unseen data**.

After this initial _pre-training_, LLMs can be fine-tuned on a supervised learning objective to perform specific tasks.
# Messages and Special Tokens
Let's looks at how they structure their generations through chat templates.

Before being fed into the LLM, all the messages in the conversation are concatenated and formatted into a single prompt that the model can understand. The model doesn't "remember" the conversation: it reads it in full every time.
![[Pasted image 20250325222430.png]]

Chat templates act as the **bridge between conversational messages (user and assistant turns) and the specific formatting requirements** of your chosen LLM. It structure the communication between the user and the agent, ensuring that every model, despite it's unique special tokens, receives the correctly formatted prompt.

Special tokens are what models use to delimit where the user and assistant turns start and end. Just as each LLM has its own EOS token, they also use different formatting rules and delimiters for the messages in the conversation.
## System Messages
Also called system prompts, define **how the model should behave**. They serve as **persistent instructions**, guiding every subsequent action.
```python
system_message = {
	"role": "system",
	"content": "You are a professional customer service agent. Always be polite, clear, and helpful"
}
```

When using agents, the System Messages also **gives information about the available tools, provides instructions to the model on how to format the actions to take, and includes guidelines on how the thought process should be segmented**.
## Conversation
Consists of alternating messages between a user and a LLM.
Chat templates help maintain context by preserving conversation history.
Templates can handle complex multi-turn conversations while maintaining context.
```python
conversation = {
	{"role": "user", "content": "I need help with my order"},
	{"role": "assistant", "content": "I'd be happy to help. Could you provide your order number?"},
	{"role": "user", "content": "It's ORDER-123"},
}
```

As explained, all messages in a conversation are concatenated and passed to the LLM as a single prompt:
```plaintext
<|im_start|>system
You are a helpful AI assistant named SmolLM, trained by Hugging Face<|im_end|>
<|im_start|>user
I need help with my order<|im_end|>
<|im_start|>assistant
I'd be happy to help. Could you provide your order number?<|im_end|>
<|im_start|>user
It's ORDER-123<|im_end|>
<|im_start|>assistant
```
## Base Model vs. Instruct Models
- A Base Model is trained on raw text data to predict the next token.
- An instruct Model is fine-tuned specifically to follow instructions and engage in conversations.

To make a Base Model behave like an Instruct Model, we need to format our prompts in a consistent way that the model can understand. This is where chat templates come in.

_ChatML_ is one such template format that structures conversations with clear role indicators (system, user, assistant).

It's important to note that a base model could be fine-tuned on different chat templates, so when we're using an instruct model we need to make sure we're using the correct chat template.
## Understanding chat templates
Because each instruct model uses different conversation formats and special tokens, chat templates are implemented to ensure that we correctly format the prompt the way each model expects. 
Chat templates describes how the list of messages will be formatted.
# What are AI Tools
A tool is a function given to the LLM. This function should fulfill a clear objective. You can create a tool for any use case!
A good tool should be something that complements the power of an LLM.

Furthermore, LLMs predict the completion of a prompt based on their training data, which means that their internal knowledge only includes events prior to their training. Therefore, if your agent needs up-to-date data you must provide it through some tool.

A Tool should contain:
- A **textual description of what the function does**.
- A _Callable_ (something to perform an action).
- _Arguments_ with types.
- (Optional) Outputs with types.
## How do tools work
What we mean when we talk about _providing tools to an Agent_, is that we **teach** the LLM about the existence of tools, and ask the model to generate text that will invoke tools when it needs to.
The LLM then will generate _text_, in the form of code, to invoke that tool. It is the responsibility of the **Agent** to parse the LLM’s output, recognize that a tool call is required, and invoke the tool on the LLM’s behalf. The output from the tool will then be sent back to the LLM, which will compose its final response for the user.
The output from a tool call is another type of message in the conversation. Tool calling steps are typically not shown to the user: the Agent retrieves the conversation, calls the tool(s), gets the outputs, adds them as a new conversation message, and sends the updated conversation to the LLM again. From the user’s point of view, it’s like the LLM had used the tool, but in fact it was our application code (the **Agent**) who did it.
## How do we give tools to an LLM
First you use the system prompt to provide textual descriptions of available tools to the model.
You have to be very precise and accurate about:
- What the tool does
- What exact inputs it expects

This is the reason why tool descriptions are usually provided using expressive but precise structures, such as JSON. But it's not necessary to do it like that, any precise format would work.

```python
# Example of a tool that will be provided to an LLM.
def calculator(a: int, b: int) -> int:
	"""Multiply two integers"""
	return a * b
```

You should then describe your tool for the LLM to understand:
```plaintext
Tool Name: calculator, Description: Multiply two integers., Arguments: a: int, b: int, Outputs: int
```
 
This textual description is what we want the LLM to know about the tool.

When we pass the previous string as part of the input to the LLM, the model will recognize it as a tool, and will know what it needs to pass as inputs and what to expect from the output.

If we want to provide additional tools, we must be consistent and always use the same format. This process can be fragile, and we might accidentally overlook some details.
## Auto-formatting tool sections
If your tool has:
- A descriptive name of what it does
- A longer description, provided by the function’s docstring comment
- The inputs and their type
- The type of the output

You can leverage your source code as specification of the tool for the LLM. Note that only the signature of your function is needed as the implementation doesn't concern the LLM.

In Python you can get the same tool specification as the previous example automatically:
```python
@tool
def calculator(a: int, b: int) -> int:
	"""Multiply two integers"""
	return a * b

print(calculator.to_string())
```

With the implementation above, we are be able to retrieve the following text automatically from the source code via the `to_string()` function provided by the decorator:

```plaintext
Tool Name: calculator, Description: Multiply two integers., Arguments: a: int, b: int, Outputs: int
```

You could then provide the tool description to your LLM as:
```python
system_message = {
	"role": "system",
	"content": """You are an AI assistant designed to help users efficiently and accurately. Your primary goal is to provide helpful, precise, and clear responses.

You have access to the following tools:
Tool Name: calculator, Description: Multiply two integers., Arguments: a: int, b: int, Outputs: int
	"""
}
```
## Understanding Agents through the Thought-Action-Observation Cycle
### Core components
Agents works in a continuous cycle of:
1. **Thinking**: The LLM part of the Agent decides what the next step should be
2. **Acting**: The Agent takes an action, by calling the tools with the associated arguments
3. **Observing**: The model reflects on the response from the tool.
### The Thought-Action-Observation Cycle
The three components work together in a [continuous loop](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit1/AgentCycle.gif).

In many Agents frameworks, **the rules and guidelines are embedded directly into the system prompt**, ensuring that every cycle adheres to a defined logic.

The system prompt might look like this:
![[Pasted image 20250403173915.png]]

### Example
Consider a weather agent, that has access to the weather API tool. and a system prompt similar to the above.
When a user asks for the weather in a given location the **thought-action-observe cycle** begins.
The agent start with the **thought** step, in which the agent generates the steps needed to fulfill the task at hand.
Considering the system prompt above, an possible internal dialogue for the agent could be:

>_The user needs current weather information for New York. I have access to a tool that fetches weather data. First, I need to call the weather API to get up-to-date details._

Based on its reasoning and the fact that the agent knows about the `get_weather` tool, the agent prepares a JSON-formatted command that calls the weather API starting the **action** step:
```json
// Note that the action specifies which tool to call and what parameter to pass.
{
  "action": "get_weather",
  "action_input": {
    "location": "New York"
  }
}
```

When the API responds, the agent starts the final step of the loop, **observation**. It'll reflect on the response of the API and extract relevant information for the task and/or next steps. In this case, will extract the weather information to add the it's final output.

With the **observation** in hand, the agent updates its internal reasoning:

>Now that i have the weather data for New York, I can compile an answer for the user.

In the **final action** the agent then generates a final response formatted as we told it to:

>**Thought**: I have the weather data now. The current weather in New York is ...

>**Final answer**: The current weather in New York is ...

The **final action** sends the answer back to the user, closing the loop.

This example shows:
1. The agent's process is cyclical: It starts with a thought, then acts by calling a tool, and finally observes the outcome. If the observation had indicated an error or incomplete data, it could have re-entered the cycle to correct its approach.
2. Tool integration: enables the agent to go beyond static knowledge.
3. Dynamic reasoning: each cycle allows the agent to incorporate fresh information (**observations**) into its reasoning (**thoughts**), ensuring that the final answer is accurate.
## Thought: Internal reasoning and the Re-Act Approach
Thoughts represents the agents internal reasoning and planning processes to solve the task.

It utilizes the agent's LLM capability to analyze information when presented in its prompt.

Think of it as the agent internal dialogue.

The agent thoughts are responsible for accessing current observations and decide what the next actions should be.

Through this process, the agent can break down complex problems into smaller, more manageable steps, reflect on past experiences, and continuously adjust its plans based on new information.
## The Re-Act approach
It's the concatenation of "Reasoning" and "Acting". It's a simple prompting technique that appends "Let's think step by step" before letting the LLM decode the next tokens.

It encourages the model decoding process toward next tokens that generate a plan, rather than a final solution, since the model is encouraged to **decompose** the problem into sub-tasks. Allows the model to consider sub-steps in more detail, which in general lead to less errors than trying to generate the final solution directly.
![[Pasted image 20250404074120.png]]

>Models like `Deepseek R1` and `OpenAI's o1` have been fine-tuned to "think before answering". These models have been trained to always include specific _thinking_ sections (enclosed between `<think>` and `</think>` special tokens). This is not just a prompting technique like ReAct, but a training method where the model learns to generate these sections after analyzing thousands of examples that show what we expect it to do.
## Actions: Enabling the agent to engage with its environment
Actions are the concrete steps an AI agent takes to interact with its environment. Each action is a deliberate operation executed by the agent.
## Type of Agent Actions
| Type of Agent          | Description                                                                                                |
| ---------------------- | ---------------------------------------------------------------------------------------------------------- |
| JSON Agent             | The Action to take is specified in JSON format.                                                            |
| Code Agent             | The Agent writes a code block that is interpreted externally.                                              |
| Function-calling Agent | It is a subcategory of the JSON Agent which has been fine-tuned to generate a new message for each action. |
One crucial part of an agent is the **ability to STOP generating new tokens when an action is complete**, and that is true for all formats of Agent. This prevents unintended output and ensures that the agent’s response is clear and precise.
## The stop and parse approach
It ensures that the agent's output is structured and predictable:
1. **Generation in structured format**: The agent outputs its intended action in a clear, predetermined format.
2. **Halting further generation**: Once the action is complete, the agent stops generating additional tokens. This prevents extra or erroneous output.
3. **Parsing the output**: An external parser reads the formatted action, determines which Tool to call, and extracts the required parameters.
## Code Agents
The idea is: instead of outputting a simple JSON object, a Code Agent generates an executable code block—typically in a high-level language like Python.
![[Pasted image 20250404075701.png]]

This approach offers several advantages:
- **Expressiveness**: Code can naturally represent complex logic, including loops, conditionals, and nested functions, providing greater flexibility than JSON.
- **Modularity and Reusability**: Generated code can include functions and modules that are reusable across different actions or tasks.
- **Enhanced Debuggability**: With a well-defined programming syntax, code errors are often easier to detect and correct.
- **Direct Integration**: Code Agents can integrate directly with external libraries and APIs, enabling more complex operations such as data processing or real-time decision making.
## Observe: Integrating Feedback to reflect and adapt
Observations are how agents perceives the consequences of its actions. They provide crucial information that fuels the Agents's thought process and guides future actions.

They are signals from the environment that guide the next cycle of thought.

In the observation phase, the agent:
- **Collects Feedback:** Receives data or confirmation that its action was successful (or not).
- **Appends Results:** Integrates the new information into its existing context, effectively updating its memory.
- **Adapts its Strategy:** Uses this updated context to refine subsequent thoughts and actions.

The Agent then uses it to decide whether additional information is needed or if it’s ready to provide a final answer.

This **iterative incorporation of feedback ensures the agent remains dynamically aligned with its goals**, constantly learning and adjusting based on real-world outcomes.
## How Are the Results Appended?
After performing an action, the framework follows these steps in order:
1. **Parse the action** to identify the function(s) to call and the argument(s) to use.
2. **Execute the action.**
3. **Append the result** as an **Observation

You can check a dummy agent implementation [here](https://github.com/us0p/dummy_agent_library_example)
## Function-Calling
Function-calling gives the model the capacity to take an action on its environment. However, the function calling capacity **is learned by the model**, and relies **less on prompting than other agents techniques**.

According to our previous learning we can clearly see that the agent didn't learn to use Tools, we just provided the list, and relied on the fact that the model was able to generalize on define a plan using these Tools.
In function-calling the agent is fine-tuned (trained) to use Tools.

Consider the concept of chat templates. In this concept, the conversation with the model is based on roles in the chat (system, assistant, user).
```python
conversation = [
	{"role": "user", "content": "I need help with my order"},
    {"role": "assistant", "content": "I'd be happy to help. Could you provide your order number?"},
    {"role": "user", "content": "It's ORDER-123"},
]
```

Function-calling brings new roles to the conversation:
- **Action**
- **Observation**
Note that most of the models formats the action to take as an "assistant" message. The chat template will then represent this as **special tokens** for function-calling.
- `[AVAILABLE_TOOLS]` – Start the list of available tools
- `[/AVAILABLE_TOOLS]` – End the list of available tools
- `[TOOL_CALLS]` – Make a call to a tool (i.e., take an “Action”)
- `[TOOL_RESULTS]` – “Observe” the result of the action
- `[/TOOL_RESULTS]` – End of the observation (i.e., the model can decode again)
```python
conversation = [
    {
        "role": "user",
        "content": "What's the status of my transaction T1001?"
    },
    {
        "role": "assistant",
        "content": "",
        "function_call": {
            "name": "retrieve_payment_status",
            "arguments": "{\"transaction_id\": \"T1001\"}"
        }
    },
    {
        "role": "tool",
        "name": "retrieve_payment_status",
        "content": "{\"status\": \"Paid\"}"
    },
    {
        "role": "assistant",
        "content": "Your transaction T1001 has been successfully paid."
    }
]
```
## Fine-Tune your model for function-calling
A model training can be divided into 3 steps:
1. **The model is pre-trained on a large quantity of data**. The output of that step is a **pre-trained model**. For instance, `google/gemma-2-2b`. It’s a base model and only knows how **to predict the next token without strong instruction following capabilities**.
2. To be useful in a chat context, the model then needs to be **fine-tuned** to follow instructions. In this step, it can be trained by model creators, the open-source community, you, or anyone. For instance, `google/gemma-2-2b-it` is an instruction-tuned model by the Google Team behind the Gemma project. 
3. The model can then be **aligned** to the creator’s preferences. For instance, a customer service chat model that must never be impolite to customers.

Usually, a complete product like Gemini or Mistral will go trough all 3 steps.

If you start from the pre-trained model it **would require more training in order to learn instruction following, chat AND function-calling**.

By starting from the instruction-tuned model, **we minimize the amount of information that our model needs to learn**.
## Low-Rank Adaptation of Large Language Models - `LoRA`
Popular and lightweight training technique that significantly reduces the number of trainable parameters.
It works by inserting a smaller number of new weights as an adapter into the model to train. This makes training with `LoRA` much faster, memory-efficient, and produces smaller model weights (a few hundred MBs), which are easier to store and share.

LoRA works by adding pairs of rank decomposition matrices to Transformer layers, typically focusing on linear layers. During training, we will “freeze” the rest of the model and will only update the weights of those newly added adapters.

By doing so, the number of **parameters** that we need to train drops considerably as we only need to update the adapter’s weights.

During inference, the input is passed into the adapter and the base model, or these adapter weights can be merged with the base model, resulting in no additional latency overhead.

LoRA is particularly useful for adapting **large** language models to specific tasks or domains while keeping resource requirements manageable. This helps reduce the memory **required** to train a model.
## Frameworks for AI agents
An agentic framework is not always needed when building an application around LLMs.
Sometimes, **predefined workflows are sufficient** to fulfill user requests, and there is no real need for an agentic framework. If the approach to build an agent is simple, like a chain of prompts, using plain code may be enough. The advantage is that the developer will have **full control and understanding of their system without abstractions**.

However, when the workflow becomes more complex, such as letting an LLM call functions or using multiple agents, these abstractions start to become helpful.
## Retrieval Augmented Generation - RAG
Combines capabilities of data retrieval and generation models to provide context-aware responses. For example, a user's query is passed to a search engine, and the retrieved results are given to the model along with the query. The model generates a response based on the query and retrieved information.

Traditional RAG systems use an LLM to answer queries based on retrieved data, agentic RAG enables intelligent control of both retrieval and generation processes, improving efficiency and accuracy.

Traditional RAG systems face key limitations, such as **relying on a single retrieval step** and focusing on direct semantic similarity with the user’s query, which may overlook relevant information.

Agentic RAG addresses these issues by allowing the agent to autonomously formulate search queries, critique retrieved results, and conduct multiple retrieval steps for a more tailored and comprehensive output.

Agentic RAG is a powerful way to use agents to answer questions about your data.
### Example
Consider an agent equipped with a `DuckDuckGo` web search tool that receives the following prompt:

`Search for luxury superhero-themed party ideas, including decorations, entertainment, and catering.`

The agent follows this process:
1. **Analyzes the Request:** The agent identifies the key elements of the query—luxury superhero-themed party planning, with focus on decor, entertainment, and catering.
2. **Performs Retrieval:** The agent leverages `DuckDuckGo` to search for the most relevant and up-to-date information, ensuring it aligns with the agent’s refined preferences for a luxurious event.
3. **Synthesizes Information:** After gathering the results, the agent processes them into a cohesive, actionable plan, covering all aspects of the party.
4. **Stores for Future Reference:** The agent stores the retrieved information for easy access when planning future events, optimizing efficiency in subsequent tasks.
## Custom Knowledge Base Tool
A vector database stores numerical representations (embedding) of text or other data, created by machine learning models. It enables semantic search by identifying similar meanings in high-dimensional data. 
## Enhanced Retrieval Capabilities
When building agentic RAG systems, the agent can employ sophisticated strategies like:
1. **Query Reformulation:** Instead of using the raw user query, the agent can craft optimized search terms that better match the target documents
2. **Multi-Step Retrieval:** The agent can perform multiple searches, using initial results to inform subsequent queries
3. **Source Integration:** Information can be combined from multiple sources like web search and local documentation
4. **Result Validation:** Retrieved content can be analyzed for relevance and accuracy before being included in responses

Effective agentic RAG systems require careful consideration of several key aspects. The agent **should select between available tools based on the query type and context**. Memory systems help maintain conversation history and avoid repetitive retrievals. Having fallback strategies ensures the system can still provide value even when primary retrieval methods fail. Additionally, implementing validation steps helps ensure the accuracy and relevance of retrieved information.
![[Pasted image 20250409073600.png]]
