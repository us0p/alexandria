To enable [RAG](agents.md##Retrieval%20Augmented%20Generation%20-%20RAG), workflow, we need to set up our data sources for retrieval, which starts with loading the documents to build up the knowledge base.

Splitting them into chunks to be processed, creating a numerical representations from text called embeddings. These embeddings, or vectors, are stored in a vector database for future retrieval.

![[Pasted image 20250721211945.png]]

Ideally, documents are split into chunks that contain sufficient context to be useful to the LLM. However, larger doesn't always mean better. If the chunks are huge, retrieval will be slow, and the LLM may struggle to extract the most relevant context from the chunk to respond to the query.

The `chunk_size` parameter is used to control this balance.
`chunk_overlap` is used to capture important information that may be lost around the boundaries between chunks.

Embeddings are numerical representations of text. Embeddings models aim to capture the "meaning" of the text, and these numbers map the text's position in a high-dimensional, or vector space.

When documents are embedded and stored, similar documents are located closer together in the vector space. When the RAG application receives a user input, it will be embedded and used to query the database, returning the most similar documents.

![[Pasted image 20250721213142.png]]
## LCEL for RAG
The retrieval chain will take a question input, insert it into the chain using `RunnablePassthrough` and assign it to "question".

`RunnablePassthrough` allows inputs to be inserted into chains unchanged. Basically, allows us to pass data through without modifying it.

We retrieve relevant documents from the vector store and assign to "context". It then integrates both of this into a prompt template pass the prompt to the model to generate an output, and parse the output into our favored format, such as a string.
![[Pasted image 20250722171452.png]]

Before building the chain, we need to create three components:
- A retriever, which is derived from our vector store.
- A prompt template for combining the user question and retrieved context.
- A model to generate the response.