# from pdfminer.high_level import extract_text
# from datetime import datetime
# import os


def save_file(content: bytes, extension: str,filename:str):
    if extension == "pdf":
        with open(f"{filename}.pdf", "wb") as temp_file:
            temp_file.write(content)
    else:
        with open("temp.txt", "w") as f:
            f.write(content.decode())


# def get_metadata(file):
#     upload_time = datetime.now().strftime("%Y-%m-%d")
#     file_name = file.filename

#     print(upload_time, file_name)
