from fastapi import FastAPI

from src.contacts.controller import router as contactsRouter
from src.utils.healthchecker import router as utilsRouter
from src.utils.env_variables import PORT

app = FastAPI()

app.include_router(utilsRouter, prefix="/api")
app.include_router(contactsRouter, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    port = int(PORT) if PORT else 8000

    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=True)
