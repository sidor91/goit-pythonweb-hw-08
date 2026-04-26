from fastapi import FastAPI

from src.contacts.controller import router as contactsRouter
from src.utils.healthchecker import router as utilsRouter

app = FastAPI()

app.include_router(utilsRouter, prefix="/api")
app.include_router(contactsRouter, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
