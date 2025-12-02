"""Input validation functions for the todo application."""

from typing import List, Union


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


def validate_task_title(title: str) -> Union[bool, str]:
    """
    Validate a task title.

    Args:
        title: The task title to validate

    Returns:
        True if valid, otherwise an error message string
    """
    if not title or not title.strip():
        return "Task title cannot be empty or contain only whitespace"

    if len(title) > 200:
        return "Task title must be less than 200 characters"

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


def validate_priority(priority: str) -> Union[bool, str]:
    """
    Validate a task priority.

    Args:
        priority: The priority level to validate ('high', 'medium', 'low')

    Returns:
        True if valid, otherwise an error message string
    """
    valid_priorities = ['high', 'medium', 'low']
    if priority not in valid_priorities:
        return f"Priority must be one of: {', '.join(valid_priorities)}"

    return True


def validate_tags(tags: List[str]) -> Union[bool, str]:
    """
    Validate a list of task tags.

    Args:
        tags: The list of tags to validate

    Returns:
        True if valid, otherwise an error message string
    """
    if not isinstance(tags, list):
        return "Tags must be a list"

    if len(tags) > 10:
        return "Maximum 10 tags allowed per task"

    for tag in tags:
        if not isinstance(tag, str):
            return f"Tag '{tag}' must be a string"

        if not (1 <= len(tag) <= 50):
            return f"Each tag must be 1-50 characters: '{tag}'"

        if not tag.replace('-', '').replace('_', '').isalnum():
            return f"Tag '{tag}' contains invalid characters. Only alphanumeric, hyphens, and underscores allowed."

    return True
