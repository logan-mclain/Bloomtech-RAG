from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.document_loaders import DirectoryLoader
from constants import *

loader = DirectoryLoader('./', glob="**/*.pdf", loader_cls=PyPDFLoader)
raw_docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=9000, chunk_overlap=400)
documents = text_splitter.split_documents(raw_docs)
print(f"Going to add {len(documents)} Documents to Pinecone")

embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
PineconeVectorStore.from_documents(documents=documents, embedding=embeddings, index_name=PINECONE_INDEX)
print("Documents uploaded to Pinecone")