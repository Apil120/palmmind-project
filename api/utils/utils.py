from datetime import datetime
from database.dbutils import connect_db,save_to_database,query_database,CONFIG_DICT
from pdfminer.high_level import extract_text
import os

COLLECTIONS = CONFIG_DICT.get("collections")
METADATA_COLLECTION = COLLECTIONS.get("metadata_database")
BOOKING_COLLECTION = COLLECTIONS.get("bookings_database")

def save_file(content: bytes, extension: str, filename: str)->dict[str,str |list[str]|bytes]:
    os.makedirs(name="uploads", exist_ok=True)
    final_name = filename + "---" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    if extension.lower() == "pdf":
        with open(rf"uploads//{final_name}.pdf", "wb") as temp_file:
            temp_file.write(content)
    else:
        with open(rf"uploads//{final_name}.txt", "w") as f:
            f.write(content.decode())

    return {
        "filename": final_name.split("---")[0] + "." + extension,
        "creation_time": final_name.split("---")[1],
        "uploads_contents":os.listdir("uploads"),
    }


def create_metadata(
    content: bytes,
    extension: str,
    filename: str,
    chunk_size: int | None,
    chunk_strat: str | None,
    database_name:str = "palmmind_project"
):
    
    
    DATABASE = connect_db(database_name=database_name)
    details_dict = save_file(content=content, extension=extension, filename=filename)
    time_upload = details_dict.get(
        "creation_time", datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    )

    file_name = details_dict.get("filename", "temp")

    metadata = {
        "filename": file_name,
        "time": time_upload,
        "chunk_size": chunk_size,
        "chunking_strat": chunk_strat,
        "id":f"FILE-{len(details_dict.get("uploads_contents"))}-{extension}"
    }
    file_id = save_to_database(collection=DATABASE[METADATA_COLLECTION],object=metadata)

    print(file_id)


def extract_text_from_files(path:str):
    extension = path.split(".")[1]

    if extension.lower() == "pdf":
        data = extract_text(pdf_file=path)
        return data
    
    with open(path,"r") as f:
        data = f.read()

    return data

def create_chunks(chunk_size:int,chunking_strat:str,path:str):
    ...