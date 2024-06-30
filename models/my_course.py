from sqlalchemy import Column, Integer, Float, CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class MyCourseDatabase(Base):
    __tablename__ = "my_course"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete=("CASCADE")))
    course_id = Column(
        Integer, ForeignKey("course.id", ondelete=("CASCADE")), unique=True
    )
    created_at = Column(Float, nullable=False)

    user = relationship("UserDatabase", back_populates="my_course")
    course = relationship("CourseDatabase", back_populates="my_course")

    __table_args__ = (
        CheckConstraint("user_id > 0", name="positive_user_id"),
        CheckConstraint("course_id > 0", name="positive_course_id"),
        CheckConstraint("created_at > 0", name="positive_created_at"),
    )

    def __init__(self, user_id, course_id, created_at, updated_at):
        self.user_id = user_id
        self.course_id = course_id
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"<My Course '{self.user_id}'>"
