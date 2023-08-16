import models
from config import get_settings
from pymongo import MongoClient

settings = get_settings()
db_name = settings.db_name
collection_name = settings.collection_name


def get_all_message(db_conn: MongoClient) -> list[models.MessageDictType]:
    """Get all messages from db

    :param MongoClient db_conn
    :return list[models.MessageDictType]
    """
    messages: list[models.MessageDictType] = [
        message for message in db_conn[db_name][collection_name].find()
    ]
    return messages
