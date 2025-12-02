"""Console menu system for the todo application."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .cli import TodoCLI


class Menu:
    """Provides menu navigation for the console todo application."""

    def __init__(self) -> None:
        """Initialize the menu system."""
        self.options: dict[str, str] = {
            "1": "Add Task",
            "2": "View Tasks",
            "3": "Complete Task",
            "4": "Delete Task",
            "5": "Exit",
        }

    def display_menu(self) -> None:
        """Display the main menu options."""
        print("\n" + "=" * 30)
        print("MAIN MENU")
        print("=" * 30)
        for key, value in self.options.items():
            print(f"{key}. {value}")
        print("=" * 30)

    def get_user_choice(self) -> str:
        """Get and validate user menu choice."""
        while True:
            try:
                choice = input("Select an option (1-5): ").strip()
                if choice in self.options:
                    return choice
                else:
                    print("Invalid option. Please select 1-5.")
            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye!")
                return "5"  # Return exit option

    def execute_choice(self, cli: "TodoCLI", choice: str) -> bool:
        """Execute the action based on user choice.

        Args:
            cli: The TodoCLI instance to execute commands on
            choice: The user's menu choice (1-5)

        Returns:
            True to continue running, False to exit
        """
        if choice == "1":
            cli._add_task()
        elif choice == "2":
            cli._list_tasks()
        elif choice == "3":
            task_id = input("Enter task ID to complete: ").strip()
            try:
                # Validate that it's a number
                int(task_id)
                cli._complete_task(f"complete {task_id}")
            except ValueError:
                print("Task ID must be a number.")
        elif choice == "4":
            task_id = input("Enter task ID to delete: ").strip()
            try:
                # Validate that it's a number
                int(task_id)
                cli._delete_task(f"delete {task_id}")
            except ValueError:
                print("Task ID must be a number.")
        elif choice == "5":
            print("Goodbye!")
            return False  # Indicate to exit
        return True  # Continue running
