from contextlib import asynccontextmanager

import config
import models
import services
from fastapi import FastAPI, Request
from pymongo import MongoClient

settings = config.get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage DB Connection opening and closing

    :param FastAPI app
    """
    app.state.db_conn = MongoClient(
        host=settings.mongo_db_url, port=settings.mongo_db_port
    )
    yield
    app.state.db_conn.close()


app = FastAPI(lifespan=lifespan)


@app.get("/messages")
def get_message(
    request: Request,
) -> list[models.Message]:
    db_conn = request.app.state.db_conn
    messages = services.get_all_messages(db_conn)
    return messages
