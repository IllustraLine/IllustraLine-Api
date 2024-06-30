from sqlalchemy import Column, Integer, Float, CheckConstraint, String
from database import Base


class BlackListTokenDatabase(Base):
    __tablename__ = "blacklist_token"
    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String, unique=True, nullable=False)
    created_at = Column(Float, nullable=False)

    __table_args__ = (
        CheckConstraint("created_at > 0", name="positive_created_at"),
        CheckConstraint("length(token) > 0", name="non_empty_token"),
    )

    def __init__(self, token, created_at):
        self.token = token
        self.created_at = created_at

    def __repr__(self):
        return f"<BlackListToken {self.token!r}>"
