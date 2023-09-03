from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def roots():
    return f'je suis dans le bon vieu temps'