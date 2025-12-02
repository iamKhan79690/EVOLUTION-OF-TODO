"""Task domain model representing a single todo item."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    """Represents a single todo item with its state and metadata.

    Attributes:
        id: Unique identifier for the task
        description: Human-readable description of the task
        is_completed: Completion status (default: False)
        created_at: Timestamp when task was created
    """

    id: int
    description: str
    is_completed: bool = False
    created_at: Optional[datetime] = None

    def __post_init__(self) -> None:
        """Validate the task after initialization."""
        if not self.description or not self.description.strip():
            raise ValueError(
                "Task description cannot be empty or contain only whitespace"
            )

        if len(self.description) > 2000:
            raise ValueError("Task description must be less than 2000 characters")

        if self.created_at is None:
            self.created_at = datetime.now()

    def complete(self) -> None:
        """Mark the task as complete."""
        self.is_completed = True

    def reopen(self) -> None:
        """Mark the task as incomplete."""
        self.is_completed = False

    def update_description(self, new_description: str) -> None:
        """Update the task description after validation.

        Args:
            new_description: New description for the task

        Raises:
            ValueError: If the new description is invalid
        """
        if not new_description or not new_description.strip():
            raise ValueError(
                "Task description cannot be empty or contain only whitespace"
            )

        if len(new_description) > 2000:
            raise ValueError("Task description must be less than 2000 characters")

        self.description = new_description
