from pydantic import BaseModel, Field


class Course(BaseModel):

    title: str
    description: str
    category_id: int = Field(alias="categoryId")
    price: float


class EditCourse(Course):

    course_id: int = Field(alias="courseId")
