# llama_pdf_summarizer

This project is a PDF summarizer built using Python. It uses the llama_cpp library to generate summaries of PDFs that are uploaded by users through a FastAPI endpoint.

## Features

- Extracts text content from PDF files using PyMuPdf.
- Summarize the extracted content using LLM llama-3
- Provides a FastAPI endpoint for uploading PDFs and retrieving summaries.

## Instalation

1. Clone the repository:

```bash
  git clone https://github.com/FelippeTN/llama_pdf_summarizer.git
  cd llama_pdf_summarizer
```

2. Create a virtual environment:

```bash
  python -m venv venv
  venv/Scripts/Activate
```

3. Install the dependencies:

```bash
  pip install -r requirements.txt
```

4. Install the LLM llama-3:

[Meta-Llama-3](https://huggingface.co/hyhf/Meta-Llama-3-8B-Instruct-Q4_K_M-GGUF/blob/main/meta-llama-3-8b-instruct-q4_k_m.gguf)

## Usage

1. Run the FastAPI server:
```bash
  python api.py
```

2. Now use and abuse the pdf summarizer 😎

[API](http://localhost:8000/docs#)

## Project Structure

- main.py: Contains the main logic for PDF extraction and summarization.
- api.py: Defines the FastAPI endpoint for handling PDF uploads and returning summaries.
- llama_config.py: The code defines a function llama_config that configures and returns an instance of the Llama model from the llama_cpp library.