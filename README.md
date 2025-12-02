# Console Todo Application

A simple console-based todo application built with Python, following domain-driven design principles with separation of concerns between domain models, business services, and UI layer.

## Features

- Add new todo items
- View all todo items (with completion status)
- Mark todo items as complete
- Delete todo items
- In-memory storage (data is lost on application restart)
- Console-based user interface with menu navigation

## Requirements

- Python 3.13+
- UV package manager (optional, but recommended)

## Installation

### Using UV (recommended)
```bash
# Install dependencies
uv sync

# Run the application
uv run src/main.py
```

### Using Python directly
```bash
# Install dependencies
pip install -e .

# Run the application
python src/main.py
```

## Usage

The application provides a menu-based interface:

1. **Add Task**: Allows you to enter a new task description
2. **View Tasks**: Shows all tasks with their completion status
3. **Complete Task**: Mark a specific task as completed by its ID
4. **Delete Task**: Remove a task by its ID
5. **Exit**: Quit the application

## Architecture

The application follows a layered architecture:

- **Domain Layer** (`src/domain/`): Contains business entities and rules
  - `task.py`: Represents a single todo item
  - `task_list.py`: Collection of tasks with operations
  - `errors.py`: Custom exception classes

- **Services Layer** (`src/services/`): Contains business logic
  - `task_service.py`: Orchestrates operations on tasks
  - `validation.py`: Input validation functions

- **UI Layer** (`src/ui/`): Console user interface
  - `cli.py`: Main CLI interface
  - `menu.py`: Menu navigation system
  - `formatters.py`: Output formatting utilities

## Testing

To run the tests:

```bash
# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=src --cov-report=term-missing
```

The application includes comprehensive unit tests for domain models, service layer, and integration tests for the CLI functionality.

## Development

The project uses:
- Ruff for linting and formatting
- Pytest for testing
- Type hints for better code documentation

## Project Status

This is Phase I of the Evolution of Todo project, featuring in-memory storage only. Future phases will introduce persistence, web UI, and other features.

## License

MIT