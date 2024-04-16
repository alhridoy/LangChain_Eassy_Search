from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter

loader = TextLoader("./essay.txt")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embedding_function = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2")

db = Chroma.from_documents(docs, embedding_function)

query = "Why do a startup that doesn't scale"
docs = db.similarity_search(query)

print(docs[0].page_content)
