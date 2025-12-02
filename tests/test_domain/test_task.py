"""Unit tests for Task domain model."""

import pytest
from datetime import datetime
from src.domain.task import Task
from src.domain.errors import TaskLimitExceeded, InvalidTaskDescription


def test_task_creation_with_valid_data():
    """Test creating a task with valid data."""
    task = Task(id=1, description="Buy groceries")

    assert task.id == 1
    assert task.description == "Buy groceries"
    assert task.is_completed is False
    assert isinstance(task.created_at, datetime)


def test_task_creation_with_completion_status():
    """Test creating a task with completion status."""
    task = Task(id=1, description="Buy groceries", is_completed=True)

    assert task.id == 1
    assert task.description == "Buy groceries"
    assert task.is_completed is True


def test_task_creation_with_empty_description():
    """Test creating a task with empty description raises error."""
    with pytest.raises(ValueError, match="Task description cannot be empty"):
        Task(id=1, description="")


def test_task_creation_with_whitespace_description():
    """Test creating a task with whitespace-only description raises error."""
    with pytest.raises(ValueError, match="Task description cannot be empty"):
        Task(id=1, description="   ")


def test_task_creation_with_long_description():
    """Test creating a task with description exceeding 2000 chars raises error."""
    long_desc = "x" * 2001

    with pytest.raises(ValueError, match="Task description must be less than 2000 characters"):
        Task(id=1, description=long_desc)


def test_task_complete_method_additional():
    """Test the complete() method sets is_completed to True."""
    task = Task(id=1, description="Buy groceries")
    assert task.is_completed is False

    task.complete()
    assert task.is_completed is True


def test_task_complete_method_already_completed():
    """Test the complete() method works on an already completed task."""
    task = Task(id=1, description="Buy groceries", is_completed=True)
    assert task.is_completed is True

    task.complete()  # Should still be completed
    assert task.is_completed is True


def test_task_reopen_method_additional():
    """Test the reopen() method sets is_completed to False."""
    task = Task(id=1, description="Buy groceries", is_completed=True)
    assert task.is_completed is True

    task.reopen()
    assert task.is_completed is False


def test_task_reopen_method_already_open():
    """Test the reopen() method works on an already open task."""
    task = Task(id=1, description="Buy groceries", is_completed=False)
    assert task.is_completed is False

    task.reopen()  # Should still be open
    assert task.is_completed is False