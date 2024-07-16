# Data Flow: User-Centric RAG Model for Indian Legal Document Analysis

## 1. System Initialization
- Pre-load common legal documents (e.g., Transfer of Property Act, Succession Act) into the vector database.
- Generate and store embeddings for these documents in the vector database- pinecone

## 2. User Interaction
- User accesses the system through the web interface.
- User selects pre-loaded documents they want to include in their analysis.
- User optionally uploads additional PDF documents.

## 3. Document Processing
- For user-uploaded documents:
  - System extracts text from PDF files.
  - Text is processed and cleaned.
  - Embeddings are generated for the processed text.
  - Embeddings are temporarily added to the vector database for the user's session.

## 4. Query Processing
- User enters a question or query through the chatbot interface.
- The query is processed and embedded using the same embedding model as the documents.

## 5. Information Retrieval
- The system performs a similarity search in the vector database using the query embedding.
- Relevant text chunks from the selected pre-loaded documents and user-uploaded documents are retrieved.

## 6. Context Preparation
- Retrieved text chunks are combined with the user's query to form a prompt for the language model.

## 7. Response Generation
- The prepared prompt is sent to the language model (e.g., OpenAI API or Google Gemini API).
- The language model generates a response based on the prompt and its training.

## 8. Response Delivery
- The generated response is sent back to the user through the chatbot interface.

## 9. Iteration
- The user can ask follow-up questions, triggering the process from step 4 again.


## Example Data Flow

1. **System Initialization**: The system is initialized with pre-loaded legal documents such as the Transfer of Property Act and the Succession Act. These documents are stored in a vector database with their corresponding embeddings.

2. **User Interaction**: A lawyer accesses the system through the web interface. They select the Transfer of Property Act and the Succession Act for their analysis session. They also upload a PDF document containing recent precedents from the Bombay High Court.

3. **Document Processing**: The system extracts text from the uploaded PDF document, cleans and processes it, and generates embeddings for the text. These embeddings are temporarily added to the vector database for the user's session.

4. **Query Processing**: The lawyer asks a question about a specific section of the Transfer of Property Act through the chatbot interface. The question is processed and embedded using the same model as the documents.

5. **Information Retrieval**: The system performs a similarity search in the vector database using the query embedding. It retrieves relevant text chunks from the selected pre-loaded documents and the user-uploaded document.

6. **Context Preparation**: The retrieved text chunks are combined with the lawyer's query to form a prompt for the language model.

7. **Response Generation**: The prepared prompt is sent to the language model (e.g., OpenAI API or Google Gemini API). The language model generates a response based on the prompt and its training.

8. **Response Delivery**: The generated response is sent back to the lawyer through the chatbot interface.



