from pdfminer.high_level import extract_text
import os

def read_file(content:bytes):
    with open("temp.pdf", "wb") as temp_file:
        temp_file.write(content)

    file_content = extract_text("temp.pdf")
    os.remove(path=os.getcwd() + "\\temp.pdf")
    return file_content
