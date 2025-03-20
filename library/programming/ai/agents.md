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