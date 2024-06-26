# LEARNING 

## About Git

### Video Resources
- [Git: Introduction and Basics](https://youtu.be/mJ-qvsxPHpY?feature=shared)

### Overview
Git is a version control system that helps track changes in code and collaborate with others. It is commonly used for software development.

### Basic Git Commands
- `git init`: Initializes an empty repository in your current path.
- `git add`: Adds files to the staging area.
  - Example: `git add .` – saves everything
  - Example: `git add index.html`
- `git commit -m "message"`: Saves the changes in your memory.
- `git log`: Shows the commit logs.
- `git checkout <commit id>`: Creates a branch.
- `git remote add origin <URL>`: Hooks up to a remote repository.
- `git push -u origin main`: Pushes to the remote repository like GitHub.

### Branches
- **Master/Main:** The default branch where everything is saved.
- **Creating a Branch:**
  - `git checkout -b <branch_name>`: Creates a new branch.
- **Switching Branches:**
  - `git checkout <branch_name>`: Switches to an existing branch.

### Merging Branches
- `git checkout main`
- `git merge <branch_name>`: Merges the specified branch into the main branch.

### Pull Request
- When working on a branch, push this branch to the GitHub repository, then make a pull request for the main owner to review and merge.

### Additional Git Commands
- `git status`: Provides information on the current state.
- `git config --global user.email "pes1202102130@pesu.pes.edu"`: Configures global user email.
- `git reset HEAD <file>`: Removes the file from the staging area.
- **Tracking Folders:**
  - Create a folder `temp`, then inside create a file `touch .gitkeep` to track the folder.
  - Remove folder: `rm -rf --temp`
- **.gitignore File:** Ignores specific folders or files listed.

### Types of Branching
- **Fast Forward:** When no changes have been made to the master branch.
- **Recursive:** When changes have been made.

### Rebasing Commits
- `git rebase master`: Applies the changes from the master branch before the changes in your branch, allowing for a fast-forward merge.

### Resolving Conflicts
- Important during rebasing or merging.

### Merge Request
- GitLab terminology for pull requests.

## Git and GitLab
- [Git and GitLab: Introduction](https://youtu.be/4lxvVj7wlZw?feature=shared)



## Generative AI and Large Language Models (LLMs)

### Video Resources
- [Generative AI in a Nutshell](https://youtu.be/2IK3DFHRFfw?feature=shared)
- [How LLMs Work](https://youtu.be/5sLYAQS9sWQ?feature=shared)
- [What is RAG?](https://youtu.be/T-D1OfcDW1M?feature=shared)

### Overview of Generative AI and LLMs
LLMs are a type of generative AI that can communicate using NLP. They are trained on large amounts of text data and refined using reinforcement learning with human feedback. 

### Retrieval-Augmented Generation (RAG)
RAG models combine LLMs with a data retrieval component to improve accuracy and reduce hallucinations.

### LangChain
An open-source orchestration framework for developing applications using LLMs. It integrates various components and solves the problem of memory in previous conversations.

### Components of RAG
1. **Document Loader and Text Processing**
   - Responsible for loading documents into the system and processing them into a suitable format for further use.

2. **Chunking the Long Documents**
   - Due to the limited context window of LLMs, long documents are divided into smaller chunks to ensure efficient processing and retrieval.

3. **Embedding of Chunked Documents**
   - Converts chunks into dense vector representations (embeddings) for efficient similarity comparisons.
   - Common techniques include Word2Vec, GloVe, BERT, and BGE.

4. **Storing the Embedding in Vector DB**
   - Embeddings are stored in a vector database for fast retrieval during query processing.
   - This allows the system to quickly access relevant information based on similarity searches.

5. **Retrieval**
   - Upon receiving a user query, the system embeds the query and retrieves the top k most similar document chunks from the vector database.
   - This ensures that the most relevant information is fetched for answering the query.

6. **Summarization**
   - Summarizes the retrieved document chunks to generate a concise and coherent response.
   - Helps in providing clear and concise answers to user queries by distilling the most important information.

7. **Evaluation**
   - Evaluates the performance of the RAG model and the quality of the generated responses.
   - This step involves measuring accuracy, relevance, and completeness to ensure continuous improvement.


### Example Use Cases
- [Q and A with RAG](https://python.langchain.com/v0.1/docs/use_cases/question_answering/)
- [RAG Based Model on Indian Constitution](https://www.youtube.com/watch?v=fIv3yPI_3-I)
- [RAG Enhanced GPT for Legal Research](https://medium.com/techmalawi/building-a-rag-enhanced-chatgpt-for-legal-research-a-case-study-on-the-case-of-attorney-general-v-370709b9b424)

### Additional Resources
- [RAG Part 1: From Naive to Advanced](https://medium.com/@j13mehul/rag-part-1-from-naive-to-advanced-cb40674a7738)
- [Hallucinations in LLM Models with Respect to Legal Domain](https://hai.stanford.edu/news/hallucinating-law-legal-mistakes-large-language-models-are-pervasive)
