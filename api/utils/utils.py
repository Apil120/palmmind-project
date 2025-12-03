from datetime import datetime
from database.dbutils import connect_db,save_to_database,query_database,CONFIG_DICT
import os

COLLECTIONS = CONFIG_DICT.get("collections")
METADATA_COLLECTION = COLLECTIONS.get("metadata_database")
BOOKING_COLLECTION = COLLECTIONS.get("bookings_database")

def save_file(content: bytes, extension: str, filename: str)->dict[str,str]:
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
        "uploads_contents":os.listdir("uploads")
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
        "id":...
    }
    save_to_database(collection=DATABASE[METADATA_COLLECTION],object=metadata)

def create_chunks(path:str,chunk_size:int,chunk_strat:str):
    ...
