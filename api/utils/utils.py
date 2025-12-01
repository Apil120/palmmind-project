from datetime import datetime

def create_metadata(content: bytes, extension: str, filename: str,chunk_size:int|None,chunk_strat:str|None):
    details_dict = save_file(content=content, extension=extension, filename=filename)
    time_upload = details_dict.get(
        "creation_time", datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    )

    file_name = details_dict.get("filename", "temp")

    print(time_upload)
    print(file_name)


def save_file(content: bytes, extension: str, filename: str):
    final_name = filename + "---" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    if extension.lower() == "pdf":
        with open(f"{final_name}.pdf", "wb") as temp_file:
            temp_file.write(content)
    else:
        with open(f"{final_name}.txt", "w") as f:
            f.write(content.decode())

    return {
        "filename": final_name.split("---")[0] + "." + extension,
        "creation_time": final_name.split("---")[1],
    }
