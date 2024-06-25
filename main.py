from flask import Flask, jsonify
from flask_cors import CORS
from config import MONGODB_URL, SECRET_KEY, POSTGRESQL_URL
from database import db_session
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from utils import (
    handle_404,
    handle_415,
    handle_429,
    handle_400,
    handle_401,
    handle_403,
    handle_405,
)
from api.auth import auth_router, auth_controller
from api.google_oauth import google_oauth_router, google_oauth_controller
from api.discord_oauth import discord_oauth_router
from api.email import email_router
from api.user import user_router


app = Flask(__name__)


CORS(app, supports_credentials=True)


app.config["SQLALCHEMY_DATABASE_URI"] = POSTGRESQL_URL
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=15)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
app.config["JWT_SECRET_KEY"] = SECRET_KEY


google_oauth_controller.google_oauth.init_app(app)
auth_controller.bcrypt.init_app(app)
auth_controller.jwt.init_app(app)


limiter = Limiter(
    get_remote_address, app=app, default_limits=[""], storage_uri=MONGODB_URL
)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.after_request
async def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response


@app.teardown_appcontext
async def shutdown_session(exception=None):
    db_session.remove()


@app.teardown_request
async def checkin_db(exception=None):
    db_session.remove()


app.register_blueprint(auth_router)
app.register_blueprint(google_oauth_router)
app.register_blueprint(discord_oauth_router)
app.register_blueprint(email_router)
app.register_blueprint(user_router)


app.register_error_handler(429, handle_429)
app.register_error_handler(404, handle_404)
app.register_error_handler(415, handle_415)
app.register_error_handler(400, handle_400)
app.register_error_handler(401, handle_401)
app.register_error_handler(403, handle_403)
app.register_error_handler(405, handle_405)
