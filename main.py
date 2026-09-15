from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello, World!"} 

@app.get("/about")
def about():
    return {"message": " sujab sujab seema   This is a FastAPI application."}