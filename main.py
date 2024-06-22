import fitz
from llama_config import llama_config

class PdfSummarizer:
    def __init__(self):
        self.llm = llama_config()
        self.pdf_content = []
        
    
    def extract_pdf(self,pdf):
        try:
            doc = fitz.open(pdf)
            if doc != []:
                for page in doc:
                    self.pdf_content.append(page.get_text())
        except Exception as e:
            print(f"ERROR: {e}")
            return None
        
        return self.pdf_content
    
    def get_response_llm(self, pdf):
        self.pdf_content = self.extract_pdf(pdf)
        if self.pdf_content is None:
            return None
        try:
            response = self.llm.create_chat_completion(
                messages = [
                    {
                        "role": "system",
                        "content": "Você é um assistente que resume pdfs."
                        },
                    {
                        "role": "user",
                        "content": f"""De acordo como o contexto do pdf, resuma-o.
                        -contexto: {self.pdf_content}"""
                    }
                ]
            )
            if self.pdf_content == []:
                return print("No content extract from pdf.")
        except Exception as e:
            print(e)
            return None
        
        return response
    
    
    