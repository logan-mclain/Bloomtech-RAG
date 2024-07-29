from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from constants import *

# Initialize the embeddings model using the specified configuration
embedding_model = OpenAIEmbeddings(model=EMBEDDING_MODEL)

# Setup Pinecone vector store for document indexing and retrieval
doc_vector_store = PineconeVectorStore(index_name=PINECONE_INDEX, embedding=embedding_model)

# Configure the retriever to fetch relevant documents based on the input query
document_retriever = doc_vector_store.as_retriever()

# Initialize the language model with the specified temperature
language_model = ChatOpenAI(temperature=0.7)

# Define a prompt template to format the query and context
prompt_template = PromptTemplate(template="{query} Context: {context}", input_variables=["query", "context"])

# Main loop to interact with the user until 'exit' command is received
user_input = ""

while user_input != "exit":
    user_input = input("Enter your query (type 'exit' to close the app)> ").strip()
    
    # Skip empty inputs
    if user_input == "":
        continue
    
    if user_input == "exit":
        print("Thank you for using the RAG App!\n\n")
        break
    
    # Retrieve relevant documents based on the user's input
    context_documents = document_retriever.get_relevant_documents(user_input)
    
    # Prepare the prompt with the retrieved context
    formatted_prompt = prompt_template.invoke({"query": user_input, "context": context_documents})
    
    # Generate a response using the language model
    response = language_model.invoke(formatted_prompt)
    
    # Display the generated response
    print(response.content)
