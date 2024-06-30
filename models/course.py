from sqlalchemy import (
    Column,
    Integer,
    Float,
    CheckConstraint,
    ForeignKey,
    String,
    LargeBinary,
    Boolean,
)
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.dialects.postgresql import JSONB


class CourseDatabase(Base):
    __tablename__ = "course"
    id = Column(Integer, primary_key=True, autoincrement=True)
    admin_id = Column(
        Integer, ForeignKey("admin_course.id", ondelete=("CASCADE")), nullable=False
    )
    admin_username = Column(
        String,
        ForeignKey("admin_course.username", ondelete=("CASCADE")),
        nullable=False,
    )
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    category = Column(String, nullable=False)
    tags = Column(JSONB, nullable=False, default=[])
    created_at = Column(Float, nullable=False)
    updated_at = Column(Float, nullable=False)
    price = Column(Float, nullable=True)
    image_name = Column(String, unique=True, nullable=False)
    course_image = Column(LargeBinary, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)

    admin_course = relationship(
        "AdminCourseDatabase", back_populates="course", foreign_keys=[admin_id]
    )
    my_course = relationship("MyCourseDatabase", back_populates="course", uselist=False)

    __table_args__ = (
        CheckConstraint("admin_id > 0", name="positive_admin_id"),
        CheckConstraint("length(admin_username) > 0", name="non_empty_admin_username"),
        CheckConstraint("length(title) > 0", name="non_empty_title"),
        CheckConstraint("length(description) > 0", name="non_empty_description"),
        CheckConstraint("length(artist) > 0", name="non_empty_artist"),
        CheckConstraint("length(category) > 0", name="non_empty_category"),
        CheckConstraint(
            "jsonb_array_length(tags) BETWEEN 1 AND 5",
            name="tags_length_between_1_and_5",
        ),
        CheckConstraint("created_at > 0", name="positive_created_at"),
        CheckConstraint("updated_at > 0", name="positive_updated_at"),
        CheckConstraint(
            "(price > 0) OR (price IS NULL)", name="positive_price_or_null"
        ),
    )

    def __init__(
        self,
        admin_id,
        admin_username,
        title,
        description,
        artist,
        category,
        tags,
        created_at,
        updated_at,
        course_image,
        price,
    ):
        self.admin_id = admin_id
        self.admin_username = admin_username
        self.title = title
        self.description = description
        self.artist = artist
        self.category = category
        self.tags = tags
        self.created_at = created_at
        self.updated_at = updated_at
        self.image_name = f"{self.created_at}_{self.admin_id}"
        self.course_image = course_image
        self.price = price

    def __repr__(self):
        return f"<Course '{self.title}'>"
