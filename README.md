# Paul Graham Essay Search 

This is a simple demo of embedding search. It splits a Paul Graham essay into chunks, gets embeddings for each chunk, loads into chromadb, and then you can query it with any phrase (searching the document)

This uses Langchain, ChromaDB, All-MiniLM-L6-v2

## Download Requirements 

```bash
pip install requirements.txt
```
Project: Building a Semantic Search Engine using LangChain and Chroma
This project demonstrates the use of LangChain and Chroma to create a semantic search engine for a collection of documents.

##Key Features
Document Loader: The project uses the TextLoader from LangChain to load a text file named essay.txt as the input document.
Text Splitting: The CharacterTextSplitter is used to split the document into smaller chunks of text, with a chunk size of 1000 characters and a chunk overlap of 0.
Embeddings: The SentenceTransformerEmbeddings is used to generate vector embeddings for the text chunks, using the pre-trained "all-MiniLM-L6-v2" model.
Vector Store: The Chroma vector store is used to store and index the text chunk embeddings.
Semantic Search: The project demonstrates a semantic search query, where the user can search for relevant text chunks based on the query.
Usage
Ensure you have the required dependencies installed, including langchain, chroma, and sentence-transformers.
Place the essay.txt file in the same directory as your Python script.
Run the provided code to load the document, split it into chunks, create the vector store, and perform a semantic search.
The search results will be printed to the console, displaying the content of the most relevant text chunk.
Next Steps
Explore different text splitting strategies and embedding models to optimize the performance of the semantic search.
Integrate the search functionality into a user-friendly web application or API.
Investigate ways to handle larger document collections and scale the vector store accordingly.
Experiment with more advanced querying and ranking techniques to improve the relevance of search results.
Feel free to customize and expand upon this project based on your specific requirements and interests in the field of semantic search and information retrieval.
## Usage

```bash
py main.py
```

## License
All code is under an MIT License.
