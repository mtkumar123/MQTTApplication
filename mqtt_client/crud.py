import config
import models
from pymongo import MongoClient

settings = config.get_settings()
db_name = settings.db_name
collection_name = settings.collection_name
db_conn = MongoClient(host=settings.mongo_db_url, port=settings.mongo_db_port)


def insert_document(document: models.Message) -> None:
    db_conn[db_name][collection_name].insert_one(document.model_dump())
