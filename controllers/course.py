from database import CourseCRUD
from utils import Validator, Miscellaneous, UserNotFound, ImageNotFound, CourseNotFound
from flask import jsonify, abort, send_file, url_for
from PIL import UnidentifiedImageError
from io import BytesIO
from config import API_URL


class CourseController:
    def __init__(self) -> None:
        self.course_database = CourseCRUD()

    async def get_course_by_id(self, user, course_id):
        if not user:
            try:
                result = await self.course_database.get(
                    "course_id", course_id=course_id
                )
            except CourseNotFound:
                return (
                    jsonify(
                        {
                            "success": False,
                            "status_code": 404,
                            "message": "course not found",
                            "data": {"course_id": course_id},
                            "errors": None,
                        }
                    ),
                    404,
                )
            return (
                jsonify(
                    {
                        "success": True,
                        "status_code": 200,
                        "message": "success get course",
                        "data": {
                            "course_id": result.id,
                            "title": result.title,
                            "description": result.description,
                            "artist": result.artist,
                            "category": result.category,
                            "tags": result.tags,
                            "price": result.price,
                            "created_at": result.created_at,
                            "updated_at": result.updated_at,
                            "is_active": result.is_active,
                            "image_url": f"{API_URL}{url_for('api course.get_image_course', course_id=result.id, course_title=result.title)}",
                        },
                        "errors": None,
                    },
                ),
                200,
            )

    async def get_course(self, user):
        if not user:
            try:
                result = await self.course_database.get("all_course")
            except CourseNotFound:
                return (
                    jsonify(
                        {
                            "success": False,
                            "status_code": 404,
                            "message": "course not found",
                            "data": None,
                            "errors": None,
                        }
                    ),
                    404,
                )
            return (
                jsonify(
                    {
                        "success": True,
                        "status_code": 200,
                        "message": "success get course",
                        "data": [
                            {
                                "course_id": data.id,
                                "title": data.title,
                                "description": data.description,
                                "artist": data.artist,
                                "category": data.category,
                                "tags": data.tags,
                                "price": data.price,
                                "created_at": data.created_at,
                                "updated_at": data.updated_at,
                                "is_active": data.is_active,
                                "image_url": f"{API_URL}{url_for('api course.get_image_course', course_id=data.id, course_title=data.title)}",
                            }
                            for data in result
                        ],
                        "errors": None,
                    }
                ),
                200,
            )

    async def get_course_image(self, course_id, course_title):
        try:
            image = await self.course_database.get(
                "image", course_id=course_id, title=course_title
            )
        except ImageNotFound:
            return (
                jsonify(
                    {
                        "success": False,
                        "status_code": 404,
                        "message": "image not found",
                        "data": {"course_id": course_id, "course_title": course_title},
                        "errors": None,
                    }
                ),
                404,
            )
        return send_file(
            BytesIO(image.course_image),
            mimetype="image/jpeg",
            download_name=f"{image.image_name}.jpg",
        )

    async def add_course(
        self, user, title, description, artist, category, tags, price, image
    ):
        if price:
            try:
                price = float(price)
            except:
                abort(415)
            else:
                if price <= 0:
                    return (
                        jsonify(
                            {
                                "success": False,
                                "status_code": 400,
                                "message": "invalid input",
                                "data": None,
                                "errors": {
                                    "price": "the number must be greater than zero"
                                },
                            }
                        ),
                        400,
                    )
        if errors := await Validator.valid_input_add_course(
            title, description, artist, category, tags, image, price
        ):
            return (
                jsonify(
                    {
                        "success": False,
                        "status_code": 400,
                        "message": "invalid input",
                        "data": None,
                        "errors": errors,
                    }
                ),
                400,
            )
        if len(tags) > 5:
            return (
                jsonify(
                    {
                        "success": False,
                        "status_code": 400,
                        "message": "invalid input",
                        "data": None,
                        "errors": {"tags": "max tags 5"},
                    }
                ),
                400,
            )
        try:
            img = await Miscellaneous.get_image_extension(image)
        except UnidentifiedImageError:
            return (
                jsonify(
                    {
                        "success": False,
                        "status_code": 400,
                        "message": "invalid image",
                        "data": None,
                        "errors": {"image": "invalid image"},
                    }
                ),
                400,
            )
        if img not in ["jpeg", "png"]:
            return (
                jsonify(
                    {
                        "success": False,
                        "status_code": 400,
                        "message": "invalid image",
                        "data": None,
                        "errors": {"image": "invalid image"},
                    }
                ),
                400,
            )
        img_byte = await Miscellaneous.image_to_large_binary(image)
        try:
            course = await self.course_database.insert(
                user.id, title, description, artist, category, tags, img_byte, price
            )
        except UserNotFound:
            return (
                jsonify(
                    {
                        "success": False,
                        "status_code": 401,
                        "message": "user does not have permission",
                        "data": {
                            "user_id": user.id,
                            "username": user.username,
                            "email": user.email,
                        },
                        "errors": None,
                    }
                ),
                401,
            )
        else:
            return "oke"
