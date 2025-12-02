"""TaskList domain model representing a collection of todo items."""

from typing import Dict, List, Optional
from .task import Task
from .errors import TaskNotFound, InvalidTaskDescription, TaskLimitExceeded


class TaskList:
    """Collection of tasks with operations to manage them.

    Attributes:
        tasks: Dictionary mapping task IDs to Task objects
        next_id: Next available ID for new tasks (auto-incrementing)
        max_tasks: Maximum number of tasks allowed in the list
    """

    def __init__(self, max_tasks: int = 1000):
        """Initialize a TaskList with a maximum capacity.

        Args:
            max_tasks: Maximum number of tasks allowed (default: 1000)
        """
        self.tasks: Dict[int, Task] = {}
        self.next_id: int = 1
        self.max_tasks = max_tasks

    def add_task(self, description: str) -> int:
        """Add a new task and return its ID.

        Args:
            description: Description of the task to add

        Returns:
            ID of the newly created task

        Raises:
            TaskLimitExceeded: If maximum task count would be exceeded
            InvalidTaskDescription: If description is invalid
        """
        if len(self.tasks) >= self.max_tasks:
            raise TaskLimitExceeded(f"Cannot exceed maximum of {self.max_tasks} tasks")

        if not description or not description.strip():
            raise InvalidTaskDescription(
                "Task description cannot be empty or contain only whitespace"
            )

        if len(description) > 2000:
            raise InvalidTaskDescription(
                "Task description must be less than 2000 characters"
            )

        task_id = self.next_id
        task = Task(id=task_id, description=description)
        self.tasks[task_id] = task
        self.next_id += 1

        return task_id

    def get_task(self, task_id: int) -> Optional[Task]:
        """Retrieve a task by ID.

        Args:
            task_id: ID of the task to retrieve

        Returns:
            Task object if found, None otherwise
        """
        return self.tasks.get(task_id)

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks in the list.

        Returns:
            List of all Task objects
        """
        return list(self.tasks.values())

    def get_pending_tasks(self) -> List[Task]:
        """Get only incomplete tasks.

        Returns:
            List of Task objects with is_completed=False
        """
        return [task for task in self.tasks.values() if not task.is_completed]

    def get_completed_tasks(self) -> List[Task]:
        """Get only completed tasks.

        Returns:
            List of Task objects with is_completed=True
        """
        return [task for task in self.tasks.values() if task.is_completed]

    def complete_task(self, task_id: int) -> bool:
        """Mark a task as complete (returns success).

        Args:
            task_id: ID of the task to complete

        Returns:
            True if the task was successfully completed

        Raises:
            TaskNotFound: If the task with the given ID doesn't exist
        """
        if task_id not in self.tasks:
            raise TaskNotFound(f"Task with ID {task_id} does not exist")

        self.tasks[task_id].complete()
        return True

    def delete_task(self, task_id: int) -> bool:
        """Remove a task from the list (returns success).

        Args:
            task_id: ID of the task to delete

        Returns:
            True if the task was successfully deleted

        Raises:
            TaskNotFound: If the task with the given ID doesn't exist
        """
        if task_id not in self.tasks:
            raise TaskNotFound(f"Task with ID {task_id} does not exist")

        del self.tasks[task_id]
        return True

    def update_task(self, task_id: int, new_description: str) -> bool:
        """Update task description (returns success).

        Args:
            task_id: ID of the task to update
            new_description: New description for the task

        Returns:
            True if the task was successfully updated

        Raises:
            TaskNotFound: If the task with the given ID doesn't exist
            InvalidTaskDescription: If the new description is invalid
        """
        if task_id not in self.tasks:
            raise TaskNotFound(f"Task with ID {task_id} does not exist")

        if not new_description or not new_description.strip():
            raise InvalidTaskDescription(
                "Task description cannot be empty or contain only whitespace"
            )

        if len(new_description) > 2000:
            raise InvalidTaskDescription(
                "Task description must be less than 2000 characters"
            )

        self.tasks[task_id].update_description(new_description)
        return True
