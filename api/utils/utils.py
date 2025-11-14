def ispdf(path:str)->bool:
    if path.endswith(".pdf"):
        return True
    
    return False