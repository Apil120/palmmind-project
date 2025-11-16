from config.config import settings

EMBED_MODEL = settings.embed_model
def create_embeddings(model=EMBED_MODEL,text:str):
    model.embed(text)  #Dummy code, need to change!!