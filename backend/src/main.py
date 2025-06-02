import os

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from constants import origins
from routers import bugs_router, login_router, users_router

from db import setup_engine

setup_engine()

app = FastAPI(root_path="/api/v1", description="Bug Tracker API server")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login_router)
app.include_router(users_router)
app.include_router(bugs_router)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=os.environ.get("PORT", 8000))
