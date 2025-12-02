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
        status = "✓" if task.is_completed else "○"
        formatted_tasks.append(f"{status} [{task.id}] {task.description}")

    return "\n".join(formatted_tasks)


def format_task(task: Task) -> str:
    """
    Format a single task for display.

    Args:
        task: Task object to format

    Returns:
        Formatted string representation of the task
    """
    status = "✓" if task.is_completed else "○"
    return f"{status} [{task.id}] {task.description}"
