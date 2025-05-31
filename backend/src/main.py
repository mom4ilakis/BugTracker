import uvicorn
from fastapi import FastAPI

from routers import bugs_router, login_router, users_router

from db import setup_engine

setup_engine()

app = FastAPI()

app.include_router(login_router)
app.include_router(users_router)
app.include_router(bugs_router)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
