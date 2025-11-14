from pdfminer.high_level import extract_text
import os


def read_file(content: bytes, extension: str):
    if extension== "pdf":
        with open("temp.pdf", "wb") as temp_file:
            temp_file.write(content)

        file_content = extract_text("temp.pdf")
        os.remove(path=os.getcwd() + "\\temp.pdf")
        return file_content

    elif extension == "txt":
        return content.decode()

    else:
        return "Invalid file format!"


