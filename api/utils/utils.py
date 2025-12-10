from datetime import datetime
from database.dbutils import connect_db, save_to_database,  CONFIG_DICT
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from pdfminer.high_level import extract_text
import os
import re
import nltk

COLLECTIONS = CONFIG_DICT.get("collections")
METADATA_COLLECTION = COLLECTIONS.get("metadata_database")
BOOKING_COLLECTION = COLLECTIONS.get("bookings_database")


def save_file(
    content: bytes, extension: str, filename: str
) -> dict[str, str | list[str] | bytes]:
    os.makedirs(name="uploads", exist_ok=True)
    final_name = filename + "---" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    if extension.lower() == "pdf":
        with open(rf"uploads//{final_name}.pdf", "wb") as temp_file:
            temp_file.write(content)
    else:
        with open(rf"uploads//{final_name}.txt", "w") as f:
            f.write(content.decode())

    return {
        "filename": final_name + "." + extension,
        "uploads_contents": os.listdir("uploads"),
    }


def create_metadata(
    content: bytes,
    extension: str,
    filename: str,
    chunk_size: int | None,
    chunk_strat: str | None,
    chunk_overlap:int|None,
    database_name: str = "palmmind_project",
):

    DATABASE = connect_db(database_name=database_name)
    details_dict = save_file(content=content, extension=extension, filename=filename)

    file_name = details_dict.get("filename", "temp")
    time_upload = file_name.split("---")[1]
    metadata = {
        "filename": file_name,
        "time": time_upload,
        "chunk_size": chunk_size,
        "chunking_strat": chunk_strat,
        "overlap":chunk_overlap,
        "id": f"FILE-{len(details_dict.get("uploads_contents"))}-{extension}",
    }
    create_chunks(path=os.path.join("uploads", file_name),chunk_size=chunk_size,chunk_strat=chunk_strat)
    save_to_database(collection=DATABASE[METADATA_COLLECTION], object=metadata)

def fixed_chunking(data:str,chunk_size:int,chunk_overlap:int):
    data = re.sub(r"s+"," ",data).strip()

    overlap = max(0,min(chunk_overlap,chunk_size-1)) #Handling cases where chunk overlap might be more than the chunk size
    chunks = []
    step = chunk_size - overlap

    for i in range(0,len(data),step):
        chunk = data[i:i + chunk_size]
        chunks.append(chunk)
        if i + chunk_size >= len(data):  # Stop once the last chunk is added
            break


    return chunks

def semantic_chunking(data,similarity_threshold = 0.70):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    sentences = nltk.sent_tokenize(data)
    embeddings = model.encode(sentences)
    chunks = []

    current_chunk = [sentences[0]]

    for i in range(1,len(sentences)):
        similarity = cosine_similarity(embeddings[i].respage(1,-1),embeddings[i-1].reshape(1,-1))[0][0]

        if similarity<similarity_threshold:
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentences[i]]

        else:
            current_chunk.append(sentences[i])

    chunks.append(" ".join(current_chunk))

    return chunks

def create_chunks(chunk_size: int, chunk_strat: str, path: str): 

    extension = path.split(".")[1]

    if extension.lower() == "pdf":
        data = extract_text(pdf_file=path)

    with open(path, "r") as f:
        data = f.read()


    if not data:
        return "Text could not be extracted!"
    
    if chunk_strat.lower() == "fixed_size":
       chunks = fixed_chunking(data,chunk_size)
       return chunks
    

    chunks = semantic_chunking(data)
    return chunks