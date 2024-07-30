from langchain.vectorstores import Pinecone as LangchainPinecone
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", api_key=os.getenv("GOOGLE_API_KEY"))


vectorstore = LangchainPinecone.from_existing_index(index_name="check1", embedding=embeddings)


llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.5)


prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {question}
Answer: """
PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)


qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(),
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)


def query_rag(question):
    result = qa_chain({"query": question})
    return result["result"], result["source_documents"]

question = "Can you talk about  Condition restraining alienation"
answer, sources = query_rag(question)
print(f"Question: {question}")
print(f"Answer: {answer}")
print("\nSources:")
for i, doc in enumerate(sources):
    print(f"Source {i+1}: {doc.metadata.get('source', 'Unknown')}")

