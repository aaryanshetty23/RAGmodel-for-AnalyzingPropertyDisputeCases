import os
import uuid
from tqdm.auto import tqdm
from typing import List
import pinecone
import langchain
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.docstore.document import Document
from dotenv import load_dotenv

load_dotenv()


def read_and_filter_doc(file_path):    
    file_loader = PyPDFLoader(file_path)
    documents = file_loader.load()
   
    if file_path == '../pdf/trp_act.pdf':
        filtered_documents = [doc for i, doc in enumerate(documents) if i >= 6]
        documents = filtered_documents
    return documents

def chunk_data(docs, chunk_size=800, chunk_overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    coherent_documents = []
    for document in docs:
        chunks = text_splitter.split_documents([document])
        coherent_documents.extend(chunks)
    return coherent_documents

def docs_to_vectors(docs: List[Document], embeddings: GoogleGenerativeAIEmbeddings):
    vectors = []
    for doc in tqdm(docs):
        embedding = embeddings.embed_query(doc.page_content)
        metadata = doc.metadata
        metadata['text'] = doc.page_content
        vectors.append({"id": str(uuid.uuid4()), "values": embedding, "metadata": metadata})
    return vectors


def process_and_upload(directory):
    api_key = os.getenv('GOOGLE_API_KEY')
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", api_key=api_key)
    pinecone_client = pinecone.Pinecone(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENVIRONMENT"))
    
    for filename in os.listdir(directory):
        
        namespace = filename[:-4]  
        pinecone_client = pinecone.Pinecone(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENVIRONMENT"))
        pc = pinecone.Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        index = pc.Index("check1")
        print("-"*80)
            
        doc_path = os.path.join(directory, filename)
        print(f"Processing and uploading {doc_path}")
        doc = read_and_filter_doc(doc_path)
        print(f"Read {len(doc)} documents from {doc_path}")
        documents = chunk_data(docs=doc)
        print(f"Split documents into {len(documents)} chunks")
        vectors = docs_to_vectors(documents, embeddings)
         
            
        index.upsert(vectors=vectors, namespace=namespace)
        print(f"Uploaded {len(vectors)} vectors to Pinecone namespace {namespace}")

process_and_upload('../pdf/')
