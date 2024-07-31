import openai
import langchain
import pinecone 
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.llms import OpenAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import google.generativeai 


load_dotenv()

def read_doc(directory):
    file_loader=PyPDFDirectoryLoader(directory)
    documents=file_loader.load()
    return documents

doc=read_doc('../pdf/')
print("LENGTH",len(doc))

def chunk_data(docs,chunk_size=800,chunk_overlap=50):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)
    doc=text_splitter.split_documents(docs)
    return docs

documents=chunk_data(docs=doc)

print("Documents Length",len(documents))

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", api_key=api_key)

print("Embedding",embeddings)



api_key = os.getenv('GOOGLE_API_KEY')

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", api_key=api_key)


sample_text = "This is a sample text to determine embedding dimensions."
embedding_vector = embeddings.embed_query(sample_text)

embedding_dimension = len(embedding_vector)
print(f"The dimension of the embedding vector is: {embedding_dimension}")


pinecone_client = pinecone.Pinecone(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENVIRONMENT"))
from pinecone import Pinecone

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("check1")

import uuid
from tqdm.auto import tqdm
from typing import List
from langchain.docstore.document import Document


def docs_to_vectors(docs: List[Document], embeddings: GoogleGenerativeAIEmbeddings):
    vectors = []
    for doc in tqdm(docs):
        embedding = embeddings.embed_query(doc.page_content)
        metadata = doc.metadata
        metadata['text'] = doc.page_content
        vectors.append((doc.metadata.get('source', 'unknown'), embedding, metadata))
    return vectors

def upload_to_pinecone(vectors, index):
    batch_size = 100
    for i in tqdm(range(0, len(vectors), batch_size)):
        batch = vectors[i:i+batch_size]
        
        
        ids = [str(uuid.uuid4()) for _ in range(len(batch))]
        
        
        vector_batch = [(ids[j], vec, meta) for j, (_, vec, meta) in enumerate(batch)]
        
        
        index.upsert(vectors=vector_batch)

    print(f"Uploaded {len(vectors)} vectors to Pinecone index ")


vectors = docs_to_vectors(documents, embeddings)

upload_to_pinecone(vectors, index)

print(f"Uploaded {len(vectors)} vectors to Pinecone index")


