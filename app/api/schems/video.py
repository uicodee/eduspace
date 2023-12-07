from pydantic import BaseModel, Field


class Video(BaseModel):

    title: str
    description: str
    preview: str
    course_id: int = Field(alias="courseId")


class EditVideo(Video):

    video_id: int = Field(alias="videoId")
