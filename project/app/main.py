import logging

from fastapi import FastAPI

from app.api import ping, summaries
from app.db import init_db

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    app = FastAPI()
    app.include_router(ping.router)
    app.include_router(summaries.router, prefix="/summaries", tags=["summaries"])
    return app


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Api starting up . . .")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Api shutting down . . .")
