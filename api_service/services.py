import crud
import models
from pymongo import MongoClient


def get_all_messages(db_conn: MongoClient) -> list[models.Message]:
    """Get all messages from crud layer

    :param _type_ db_conn
    :return list[models.Message]
    """
    messages = crud.get_all_message(db_conn)
    return [models.Message(**message) for message in messages]
