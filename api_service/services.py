import crud
import models


def get_all_messages(db_conn) -> list[models.Message]:
    messages = crud.get_all_message(db_conn)
    return [models.Message(**message) for message in messages]
