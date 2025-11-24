# from pdfminer.high_level import extract_text
from datetime import datetime
# import os


def save_file(content: bytes, extension: str,filename:str):
    time_of_creation = "-"+datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    if extension == "pdf":
        with open(f"{filename+time_of_creation}.pdf", "wb") as temp_file:
            temp_file.write(content)
    else:
        with open(f"{filename+time_of_creation}.txt", "w") as f:
            f.write(content.decode())

#TODO:: Make a new metadata wala funciton, utilise the variables from save_file wala func.