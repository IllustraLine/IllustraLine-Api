from flask import Blueprint, request
from controllers import CourseController
from flask_jwt_extended import jwt_required, current_user

course_router = Blueprint("api course", __name__)
course_controller = CourseController()


@course_router.get("/illustra-line/v1/course/<string:course_title>")
@jwt_required(optional=True)
async def search_course(course_title):
    return await course_controller.search_course(current_user, course_title)


@course_router.get("/illustra-line/v1/course/<int:course_id>/<string:course_title>")
async def get_image_course(course_id, course_title):
    return await course_controller.get_course_image(course_id, course_title)


@course_router.get("/illustra-line/v1/course")
@jwt_required(optional=True)
async def get_course():
    return await course_controller.get_course(current_user)


@course_router.get("/illustra-line/v1/course/<int:course_id>")
@jwt_required(optional=True)
async def get_course_by_id(course_id):
    return await course_controller.get_course_by_id(current_user, course_id)


@course_router.post("/illustra-line/v1/course")
@jwt_required()
async def add_course():
    data = request.form
    file = request.files
    title = data.get("title")
    description = data.get("description")
    artist = data.get("artist")
    category = data.get("category")
    tags = data.get("tags").split(",")
    price = data.get("price")
    image = file.get("image")
    return await course_controller.add_course(
        current_user, title, description, artist, category, tags, price, image
    )
