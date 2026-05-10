from docx import Document
import os

def save_as_docx(text: str, filename: str):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    doc = Document()

    for line in text.split("\n"):
        doc.add_paragraph(line)

    doc.save(filename)
    return filename
