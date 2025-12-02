"""Input validation functions for the todo application."""

from typing import Union


def validate_task_description(description: str) -> Union[bool, str]:
    """
    Validate a task description.

    Args:
        description: The task description to validate

    Returns:
        True if valid, otherwise an error message string
    """
    if not description or not description.strip():
        return "Task description cannot be empty or contain only whitespace"

    if len(description) > 2000:
        return "Task description must be less than 2000 characters"

    return True


def validate_task_id(task_id: int) -> Union[bool, str]:
    """
    Validate a task ID.

    Args:
        task_id: The task ID to validate

    Returns:
        True if valid, otherwise an error message string
    """
    if not isinstance(task_id, int) or task_id <= 0:
        return "Task ID must be a positive integer"

    return True


def validate_task_limit(current_count: int, max_limit: int = 1000) -> Union[bool, str]:
    """
    Validate that the task limit is not exceeded.

    Args:
        current_count: Current number of tasks
        max_limit: Maximum allowed tasks

    Returns:
        True if valid, otherwise an error message string
    """
    if current_count >= max_limit:
        return f"Cannot exceed maximum of {max_limit} tasks"

    return True
