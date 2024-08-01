import os
import uuid
from tqdm.auto import tqdm
from typing import List
import pinecone
import langchain
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.docstore.document import Document
from dotenv import load_dotenv

load_dotenv()

def read_and_filter_doc(directory, skip_pages=6):
    file_loader = PyPDFDirectoryLoader(directory)
    documents = file_loader.load()
    filtered_documents = [doc for i, doc in enumerate(documents) if i >= skip_pages]
    return filtered_documents

doc = read_and_filter_doc('../pdf/')
print("LENGTH", len(doc))

def chunk_data(docs, chunk_size=1000, chunk_overlap=70):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    coherent_documents = []
    for document in docs:
        chunks = text_splitter.split_documents([document])
        coherent_documents.extend(chunks)
    return coherent_documents

documents = chunk_data(docs=doc)
print("Documents Length", len(documents))

api_key = os.getenv('GOOGLE_API_KEY')
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", api_key=api_key)
print("Embedding", embeddings)

pinecone_client = pinecone.Pinecone(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENVIRONMENT"))
pc = pinecone.Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("check1")

def docs_to_vectors(docs: List[Document], embeddings: GoogleGenerativeAIEmbeddings):
    vectors = []
    for doc in tqdm(docs):
        embedding = embeddings.embed_query(doc.page_content)
        metadata = doc.metadata
        metadata['text'] = doc.page_content
        vectors.append((str(uuid.uuid4()), embedding, metadata))
    return vectors

def upload_to_pinecone(vectors, index):
    batch_size = 100
    for i in tqdm(range(0, len(vectors), batch_size)):
        batch = vectors[i:i+batch_size]
        index.upsert(vectors=batch)
    print(f"Uploaded {len(vectors)} vectors to Pinecone index")

vectors = docs_to_vectors(documents, embeddings)
upload_to_pinecone(vectors, index)
