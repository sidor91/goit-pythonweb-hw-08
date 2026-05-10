from fastapi import FastAPI

from src.contacts.controller import router as contacts_router
from src.utils.healthchecker import router as utils_router
from src.auth.controller import router as auth_router
from src.users.controller import router as users_router
from src.utils.env_variables import settings

app = FastAPI()

app.include_router(utils_router, prefix="/api")
app.include_router(contacts_router, prefix="/api")
app.include_router(auth_router, prefix="/api")
app.include_router(users_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=settings.PORT, reload=True)
