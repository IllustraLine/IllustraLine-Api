from .database import Database
from .config import db_session, init_db
from models import CourseDatabase


class MyCourse(Database):
    def __init__(self) -> None:
        super().__init__()
        init_db()

    async def insert(self):
        pass

    async def update(self):
        pass

    async def delete(self):
        pass

    async def get(self):
        pass
