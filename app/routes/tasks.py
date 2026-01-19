from fastapi import APIRouter, HTTPException, status
from app.storage import load_data, save_data
from app.schemas import TaskOut, TaskDto

import uuid

router = APIRouter(prefix="/api/v1/tasks", tags=["tasks"])


@router.get("/", response_model=list[TaskOut])
async def get_tasks():
    """Retrieve a list of tasks"""
    tasks = load_data()
    return tasks

@router.get("/{task_id}", response_model=TaskOut)
async def get_task(task_id: str):
    """Retrieve a single task by ID"""
    tasks = load_data()
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskDto):
    """Create a new task"""
    print(task)
    tasks = load_data()
    new_task = {
        "id": str(uuid.uuid4()),
        "name": task.name,
        "description": task.description,
        "priority": task.priority,
        "dueDate": task.dueDate,
        "isDone": task.isDone,
    }
    tasks.append(new_task)
    save_data(tasks)
    return new_task


@router.put("/{task_id}", response_model=TaskOut)
async def update_task(task_id: str, task: TaskDto):
    """Update an existing task"""
    tasks = load_data()
    for index, existing_task in enumerate(tasks):
        if existing_task["id"] == task_id:
            updated_task = {
                "id": task_id,
                "name": task.name,
                "description": task.description,
                "priority": task.priority,
                "dueDate": task.dueDate,
                "isDone": task.isDone,
            }
            tasks[index] = updated_task
            save_data(tasks)
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: str):
    """Delete a task"""
    tasks = load_data()
    for index, existing_task in enumerate(tasks):
        if existing_task["id"] == task_id:
            tasks.pop(index)
            save_data(tasks)
            return
    raise HTTPException(status_code=404, detail="Task not found")
