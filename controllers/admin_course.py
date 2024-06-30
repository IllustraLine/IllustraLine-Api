from database import AdminCourseCRUD
import datetime
from sqlalchemy.exc import IntegrityError
from flask import jsonify
from utils import UserNotFound, UserInvalid


class AdminCourseController:
    def __init__(self) -> None:
        self.admin_course = AdminCourseCRUD()

    async def add_admin(self, user, username):
        created_at = datetime.datetime.now(datetime.timezone.utc).timestamp()
        try:
            await self.admin_course.insert(user.id, username, created_at, created_at)
        except UserNotFound:
            return (
                jsonify(
                    {
                        "success": False,
                        "status_code": 404,
                        "message": "admin is not found",
                        "data": {"user_id": user.id, "username": username},
                        "errors": None,
                    }
                ),
                404,
            )
        except IntegrityError:
            return (
                jsonify(
                    {
                        "success": False,
                        "status_code": 400,
                        "message": "admin is already registered",
                        "data": {
                            "user_id": user.id,
                            "username": username,
                            "email": user.email,
                        },
                        "errors": None,
                    }
                ),
                400,
            )
        except UserInvalid:
            return (
                jsonify(
                    {
                        "success": False,
                        "status_code": 401,
                        "message": "user does not have permission",
                        "data": {
                            "user_id": user.id,
                            "username": username,
                            "email": user.email,
                        },
                        "errors": None,
                    }
                ),
                401,
            )
        else:
            return (
                jsonify(
                    {
                        "success": True,
                        "status_code": 201,
                        "message": "success add admin",
                        "data": {
                            "user_id": user.id,
                            "username": username,
                            "email": user.email,
                            "created_at": created_at,
                        },
                        "errors": None,
                    }
                ),
                201,
            )
