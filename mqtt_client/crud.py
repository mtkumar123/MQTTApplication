import models
from logger import mqtt_logger
from pymongo import MongoClient
from pymongo.errors import PyMongoError


def insert_document(
    db_conn: MongoClient,
    db_name: str,
    db_collection: str,
    document: models.Message,
) -> None:
    """Insert message to db

    :param models.Message document
    """
    try:
        db_conn[db_name][db_collection].insert_one(document.model_dump())
    except PyMongoError:
        mqtt_logger.exception("Unable insert document to MongoDB")
