# AI for Kitestring Employees Regarding the Company Handbook Policy

## Overview

- The purpose of this project is to understand RAG as a concept. In this example, I am storing Kitestring's handbook in Pinecone as a vector database so that the user can ask questions regarding our handbook's policies and the LLM will use RAG to lookup those answers. 

## Installation

### Prerequisites

- Python 3.8 or higher
- pip3

### Steps to Install

- Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

- Create and activate a virtual environment (recommended):

```bash
python -m venv venv
source
venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

-Install dependencies and export keys

```bash
pip3 install -r requirements.txt
export OPENAI_API_KEY=
export PINECONE_API_KEY=
```
