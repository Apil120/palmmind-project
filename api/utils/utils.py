from pdfminer.high_level import extract_text
from datetime import datetime
import os


def read_file(content: bytes, extension: str):
    if extension == "pdf":
        with open("temp.pdf", "wb") as temp_file:
            temp_file.write(content)

        file_content = extract_text("temp.pdf")
        os.remove(path=os.getcwd() + "\\temp.pdf")
        return file_content

    elif extension == "txt":
        return content.decode()

    else:
        return "Invalid file format!"


def get_metadata(file):
    upload_time = datetime.now().strftime("%Y-%m-%d")
    file_name = file.filename

    print(upload_time, file_name)
