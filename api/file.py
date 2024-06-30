from flask import Blueprint, request

upload_file_router = Blueprint("api upload", __name__)


@upload_file_router.post("/illustra-line/v1/upload")
async def add_course():
    data = request.data
    file = request.files
    print(file)
    return "hello world"
