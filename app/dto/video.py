from pydantic import Field

from app.dto import Base


class Video(Base):

    title: str
    description: str
    views: int
    preview: str
    course_id: int = Field(alias="courseId")
