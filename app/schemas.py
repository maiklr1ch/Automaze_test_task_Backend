from pydantic import BaseModel, Field

class TaskDto(BaseModel):
  name: str = Field(example="Task name", min_length=1, max_length=100)
  description: str = Field(..., example="Task description", min_length=0, max_length=500)
  priority: int = Field(..., example=10, ge=1, le=10)
  dueDate: str = Field(..., example="2023-12-31T23:59:59Z")
  isDone: bool = Field(default=False, example=False)

class TaskOut(BaseModel):
  id: str = Field(example=1)
  name: str = Field(example="Task name")
  description: str = Field(example="Task description")
  priority: int = Field(example=10)
  dueDate: str = Field(example="2023-12-31T23:59:59Z")
  isDone: bool = Field(example=False)