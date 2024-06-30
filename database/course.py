from .database import Database
from .config import db_session, init_db
from models import CourseDatabase, AdminCourseDatabase, UserDatabase
import datetime
from sqlalchemy import desc, and_
from utils import UserNotFound, ImageNotFound, CourseNotFound


class CourseCRUD(Database):
    def __init__(self) -> None:
        super().__init__()
        init_db()

    async def insert(
        self, user_id, title, description, artist, category, tags, image, price
    ):
        if data := (
            db_session.query(UserDatabase, AdminCourseDatabase)
            .select_from(UserDatabase)
            .join(AdminCourseDatabase, AdminCourseDatabase.user_id == UserDatabase.id)
            .filter(UserDatabase.id == user_id)
            .order_by(desc(UserDatabase.created_at))
            .first()
        ):
            user, admin = data
            created_at = datetime.datetime.now(datetime.timezone.utc).timestamp()
            course = CourseDatabase(
                admin.id,
                admin.username,
                title,
                description,
                artist,
                category,
                tags,
                created_at,
                created_at,
                image,
                price,
            )
            admin.updated_at = created_at
            user.updated_at = created_at
            db_session.add(course)
            db_session.commit()
            return course
        raise UserNotFound

    async def update(self):
        pass

    async def delete(self):
        pass

    async def get(self, category, **kwargs):
        course_id = kwargs.get("course_id")
        title = kwargs.get("title")
        if category == "image":
            if data := (
                CourseDatabase.query.filter(
                    and_(CourseDatabase.id == course_id, CourseDatabase.title == title)
                )
                .order_by(desc(CourseDatabase.created_at))
                .first()
            ):
                return data
            raise ImageNotFound
        elif category == "all_course":
            if data := (
                CourseDatabase.query.order_by(desc(CourseDatabase.created_at)).all()
            ):
                return data
            raise CourseNotFound
        elif category == "course_id":
            if data := (
                CourseDatabase.query.filter(CourseDatabase.id == course_id)
                .order_by(desc(CourseDatabase.created_at))
                .first()
            ):
                return data
            raise CourseNotFound
