"""Command-line interface for the todo application."""

import sys
from typing import TYPE_CHECKING
from ..services.task_service import TaskService
from .formatters import format_task_list
from .menu import Menu

if TYPE_CHECKING:
    # This import is used by menu.py
    pass


class TodoCLI:
    """Command-line interface for interacting with the todo application.

    Attributes:
        task_service: The TaskService instance used for task operations
        menu: The Menu instance for navigation
    """

    def __init__(self, task_service: TaskService):
        """Initialize the CLI with a task service.

        Args:
            task_service: TaskService instance to use for operations
        """
        self.task_service = task_service
        self.menu = Menu()

    def run(self):
        """Run the main CLI loop."""
        print("Welcome to the Console Todo Application!")

        while True:
            try:
                self.menu.display_menu()
                choice = self.menu.get_user_choice()

                should_continue = self.menu.execute_choice(self, choice)
                if not should_continue:
                    sys.exit(0)

            except KeyboardInterrupt:
                print("\nGoodbye!")
                sys.exit(0)
            except Exception as e:
                print(f"An error occurred: {e}")

    def run_old_style(self):
        """Run the main CLI loop using old command-style interface."""
        print("Available commands: add, list, complete, delete, exit")

        while True:
            try:
                command = input("\nEnter command: ").strip().lower()

                if command == "add":
                    self._add_task()
                elif command == "list":
                    self._list_tasks()
                elif command.startswith("complete "):
                    self._complete_task(command)
                elif command.startswith("delete "):
                    self._delete_task(command)
                elif command == "exit":
                    print("Goodbye!")
                    sys.exit(0)
                else:
                    print(
                        f"Unknown command: {command}. Available: add, list, complete, delete, exit"
                    )

            except KeyboardInterrupt:
                print("\nGoodbye!")
                sys.exit(0)
            except Exception as e:
                print(f"An error occurred: {e}")

    def _add_task(self):
        """Handle adding a new task."""
        try:
            description = input("Enter task description: ").strip()
            if not description:
                print("Task description cannot be empty.")
                return

            task = self.task_service.create_task(description)
            print(f"Task added with ID: {task.id}")
        except Exception as e:
            print(f"Error adding task: {e}")

    def _list_tasks(self):
        """Handle listing all tasks."""
        try:
            tasks = self.task_service.get_all_tasks()

            print("\nYour tasks:")
            print(format_task_list(tasks))
        except Exception as e:
            print(f"Error listing tasks: {e}")

    def _complete_task(self, command: str):
        """Handle completing a task.

        Args:
            command: Command string in format "complete <task_id>"
        """
        try:
            parts = command.split(" ", 1)
            if len(parts) != 2:
                print("Usage: complete <task_id>")
                return

            task_id_str = parts[1]
            try:
                task_id = int(task_id_str)
            except ValueError:
                print("Task ID must be a number.")
                return

            task = self.task_service.mark_task_complete(task_id)
            print(f"Task {task.id} marked as complete: {task.description}")
        except Exception as e:
            print(f"Error completing task: {e}")

    def _delete_task(self, command: str):
        """Handle deleting a task.

        Args:
            command: Command string in format "delete <task_id>"
        """
        try:
            parts = command.split(" ", 1)
            if len(parts) != 2:
                print("Usage: delete <task_id>")
                return

            task_id_str = parts[1]
            try:
                task_id = int(task_id_str)
            except ValueError:
                print("Task ID must be a number.")
                return

            success = self.task_service.delete_task(task_id)
            if success:
                print(f"Task {task_id} deleted successfully.")
            else:
                print(f"Task {task_id} not found.")
        except Exception as e:
            print(f"Error deleting task: {e}")
