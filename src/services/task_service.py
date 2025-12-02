"""Task service implementing business logic for task operations."""

from typing import List, Optional
from ..domain.task import Task
from ..domain.task_list import TaskList
from ..domain.errors import TaskNotFound, InvalidTaskDescription, TaskLimitExceeded
from .validation import validate_task_description, validate_task_id, validate_task_limit


class TaskService:
    """Business logic layer that orchestrates operations on tasks.

    Attributes:
        task_list: The TaskList instance to operate on
    """

    def __init__(self, task_list: Optional[TaskList] = None):
        """Initialize TaskService with a TaskList.

        Args:
            task_list: TaskList instance to operate on (creates new if None)
        """
        self.task_list = task_list or TaskList()

    def create_task(self, description: str) -> Task:
        """Create a new task with validation.

        Args:
            description: Description of the new task

        Returns:
            The created Task object

        Raises:
            InvalidTaskDescription: If the description is invalid
            TaskLimitExceeded: If the task limit would be exceeded
        """
        validation_result = validate_task_description(description)
        if validation_result is not True:
            raise InvalidTaskDescription(validation_result)

        validation_result = validate_task_limit(len(self.task_list.tasks))
        if validation_result is not True:
            raise TaskLimitExceeded(validation_result)

        task_id = self.task_list.add_task(description)
        return self.task_list.get_task(task_id)

    def get_task(self, task_id: int) -> Task:
        """Get a specific task.

        Args:
            task_id: ID of the task to retrieve

        Returns:
            The requested Task object

        Raises:
            ValueError: If task_id is invalid
            TaskNotFound: If task with given ID doesn't exist
        """
        validation_result = validate_task_id(task_id)
        if validation_result is not True:
            raise ValueError(validation_result)

        task = self.task_list.get_task(task_id)
        if task is None:
            raise TaskNotFound(f"Task with ID {task_id} does not exist")

        return task

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks.

        Returns:
            List of all Task objects
        """
        return self.task_list.get_all_tasks()

    def mark_task_complete(self, task_id: int) -> Task:
        """Mark task as complete.

        Args:
            task_id: ID of the task to mark complete

        Returns:
            The updated Task object

        Raises:
            ValueError: If task_id is invalid
            TaskNotFound: If task with given ID doesn't exist
        """
        validation_result = validate_task_id(task_id)
        if validation_result is not True:
            raise ValueError(validation_result)

        self.task_list.complete_task(task_id)
        return self.task_list.get_task(task_id)

    def delete_task(self, task_id: int) -> bool:
        """Delete a task.

        Args:
            task_id: ID of the task to delete

        Returns:
            True if the task was successfully deleted, False otherwise

        Raises:
            ValueError: If task_id is invalid
        """
        validation_result = validate_task_id(task_id)
        if validation_result is not True:
            raise ValueError(validation_result)

        try:
            return self.task_list.delete_task(task_id)
        except TaskNotFound:
            return False

    def update_task(self, task_id: int, description: str) -> Task:
        """Update a task description.

        Args:
            task_id: ID of the task to update
            description: New description for the task

        Returns:
            The updated Task object

        Raises:
            ValueError: If task_id or description is invalid
            TaskNotFound: If task with given ID doesn't exist
            InvalidTaskDescription: If the new description is invalid
        """
        validation_result = validate_task_id(task_id)
        if validation_result is not True:
            raise ValueError(validation_result)

        validation_result = validate_task_description(description)
        if validation_result is not True:
            raise InvalidTaskDescription(validation_result)

        self.task_list.update_task(task_id, description)
        return self.task_list.get_task(task_id)
