from flask import Blueprint
from controllers import AdminCourseController
from flask_jwt_extended import jwt_required, current_user

admin_course_router = Blueprint("api admin course", __name__)
admin_course_controller = AdminCourseController()


@admin_course_router.post("/illustra-line/v1/admin-course/<string:username>")
@jwt_required()
async def add_admin(username):
    return await admin_course_controller.add_admin(current_user, username)
