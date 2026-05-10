from pypdf import PdfReader
import os

def load_pdf_text(pdf_path):

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"找不到 PDF 文件：{pdf_path}")
    
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text +"\n"

        if not text.strip():
            raise ValueError("没有从 PDF 中提取到文字，可能是扫描版 PDF 或图片型 PDF。")

    return text