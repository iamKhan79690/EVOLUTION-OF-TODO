"""Output formatting utilities for the todo application."""

from typing import List
from src.domain.task import Task


def format_task_list(tasks: List[Task]) -> str:
    """
    Format a list of tasks for display.

    Args:
        tasks: List of Task objects to format

    Returns:
        Formatted string representation of the tasks
    """
    if not tasks:
        return "No tasks found."

    formatted_tasks = []
    for task in tasks:
        status = "[x]" if task.is_completed else "[ ]"
        priority = f"({task.priority.capitalize()})" if task.priority else ""
        tags = f"[{', '.join(task.tags)}]" if task.tags else ""

        task_parts = [status, f"{task.id}. {task.description}"]
        if priority:
            task_parts.insert(1, priority)
        if tags:
            task_parts.append(tags)

        formatted_tasks.append(" ".join(task_parts))

    return "\n".join(formatted_tasks)


def format_task(task: Task) -> str:
    """
    Format a single task for display.

    Args:
        task: Task object to format

    Returns:
        Formatted string representation of the task
    """
    status = "[x]" if task.is_completed else "[ ]"
    priority = f"({task.priority.capitalize()})" if task.priority else ""
    tags = f"[{', '.join(task.tags)}]" if task.tags else ""

    task_parts = [status, f"{task.id}. {task.description}"]
    if priority:
        task_parts.insert(1, priority)
    if tags:
        task_parts.append(tags)

    return " ".join(task_parts)
