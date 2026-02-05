from fastapi import FastAPI

app = FastAPI(title="T11PRH96 Backend", version="0.1.0")


@app.get("/")
async def home():
    return {"message": "Hello world!"}
