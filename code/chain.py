from langchain.vectorstores import Pinecone as LangchainPinecone
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
load_dotenv()


embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", api_key=os.getenv("GOOGLE_API_KEY"))


def init_vectorstore(namespace):
    return LangchainPinecone.from_existing_index(index_name="check1", embedding=embeddings, namespace=namespace)


llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.5)

prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {question}
Answer: """
PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)


def setup_qa_chain(namespace):
    vectorstore = init_vectorstore(namespace)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff", 
        retriever=vectorstore.as_retriever(),
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )
    return qa_chain


def query_rag(question, namespace):
    qa_chain = setup_qa_chain(namespace)
    result = qa_chain({"query": question})
    
   
    answer = result["result"]
    sources = result["source_documents"]
    
    
    print("Context used for generating the answer:")
    for i, doc in enumerate(sources):
        print(f"Context {i+1}:")
        print(doc.page_content)
        print("-" * 80)
    
    return answer, sources


if __name__ == "__main__":
    question = "According to the transfer of property act can you talk about what may be transferred?"
    namespace = "The_Indian_Contract_Act_1872"
    answer, sources = query_rag(question, namespace)
    print(f"Question: {question}")
    print(f"Answer: {answer}")
