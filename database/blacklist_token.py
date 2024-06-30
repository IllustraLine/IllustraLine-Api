from .database import Database
from .config import db_session, init_db
from models import BlackListTokenDatabase


class BlackListTokenCRUD(Database):
    def __init__(self) -> None:
        super().__init__()
        init_db()

    async def insert(self, token, created_at):
        blacklist_token = BlackListTokenDatabase(token, created_at)
        db_session.add(blacklist_token)
        db_session.commit()
        return blacklist_token

    async def update(self):
        pass

    async def delete(self):
        pass

    async def get(self):
        pass
