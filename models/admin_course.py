from sqlalchemy import Column, Integer, Float, CheckConstraint, ForeignKey, String
from sqlalchemy.orm import relationship
from database import Base
from .course import CourseDatabase


class AdminCourseDatabase(Base):
    __tablename__ = "admin_course"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(
        Integer,
        ForeignKey("user.id", ondelete=("CASCADE")),
        unique=True,
        nullable=False,
    )
    username = Column(String, unique=True, nullable=False)
    created_at = Column(Float, nullable=False)
    updated_at = Column(Float, nullable=False)

    user = relationship("UserDatabase", back_populates="admin_course")
    course = relationship(
        "CourseDatabase",
        back_populates="admin_course",
        foreign_keys=[CourseDatabase.admin_id],
        uselist=False,
    )

    __table_args__ = (
        CheckConstraint("user_id > 0", name="positive_user_id"),
        CheckConstraint("length(username) > 0", name="non_empty_username"),
        CheckConstraint("created_at > 0", name="positive_created_at"),
        CheckConstraint("updated_at > 0", name="positive_updated_at"),
    )

    def __init__(self, user_id, username, created_at, updated_at):
        self.user_id = user_id
        self.username = username
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"<Admin Course '{self.username}'>"
