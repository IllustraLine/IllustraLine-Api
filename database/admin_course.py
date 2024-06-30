from .database import Database
from .config import db_session, init_db
from models import AdminCourseDatabase, UserDatabase
from utils import UserInvalid, UserNotFound
from sqlalchemy import desc


class AdminCourseCRUD(Database):
    def __init__(self) -> None:
        super().__init__()
        init_db()

    async def insert(self, user_id, username, created_at, updated_at):
        if admin := (
            UserDatabase.query.filter(UserDatabase.id == user_id)
            .order_by(desc(UserDatabase.created_at))
            .first()
        ):
            if admin.is_admin:
                admin_course = AdminCourseDatabase(
                    user_id, username, created_at, updated_at
                )
                admin.updated_at = created_at
                db_session.add(admin_course)
                db_session.commit()
                return admin_course
            raise UserInvalid
        raise UserNotFound

    async def update(self):
        pass

    async def delete(self):
        pass

    async def get(self):
        pass
