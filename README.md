# 📝 EVOLUTION-OF-TODO

A sophisticated console-based todo application built with Python, featuring intelligent task management capabilities including priorities, tags, due dates, recurring tasks, and advanced search/filter/sort functionality.

[![Python](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/iamKhan79690/EVOLUTION-OF-TODO/actions)

## 🌟 Features

### ✅ **Core Features**
- **Add/View/Edit/Delete Tasks** - Complete CRUD operations
- **Mark Tasks Complete** - Track progress with completion status
- **Priority Management** - Assign High/Medium/Low priorities to tasks
- **Tagging System** - Categorize tasks with custom tags for better organization
- **Due Dates & Reminders** - Set deadlines with time-based notifications

### 🔄 **Advanced Features**
- **Recurring Tasks** - Auto-reschedule repeating tasks (daily, weekly, monthly, yearly)
- **Keyword Search** - Find tasks instantly with search functionality
- **Smart Filtering** - Filter by priority, tags, status, and due dates
- **Flexible Sorting** - Sort by priority, title, or due date
- **Console Notifications** - Time-based reminder system with configurable alerts

### 🔧 **Architecture Highlights**
- **Domain-Driven Design** - Clean separation between domain models, business logic, and UI
- **In-Memory Storage** - Fast and lightweight (Phase I implementation)
- **Extensible Design** - Easy to extend with new features
- **Comprehensive Testing** - 113+ tests ensuring reliability

## 📋 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Architecture](#-architecture)
- [Testing](#-testing)
- [Development](#-development)
- [Contributing](#-contributing)
- [License](#-license)

## 🛠️ Installation

### Prerequisites
- Python 3.13+
- UV package manager (recommended)

### Using UV (Recommended)
```bash
# Clone the repository
git clone https://github.com/iamKhan79690/EVOLUTION-OF-TODO.git
cd EVOLUTION-OF-TODO

# Install dependencies
uv sync

# Run the application
uv run src/main.py
```

### Using Python directly
```bash
# Clone the repository
git clone https://github.com/iamKhan79690/EVOLUTION-OF-TODO.git
cd EVOLUTION-OF-TODO

# Install dependencies
pip install -e .

# Run the application
python src/main.py
```

## 🚀 Usage

The application provides a comprehensive menu-based interface:

### Main Menu Options
```
┌─────────────────────────────────────┐
│            MAIN MENU                │
├─────────────────────────────────────┤
│ 1. Add Task                         │
│ 2. View Tasks                       │
│ 3. Complete Task                    │
│ 4. Delete Task                      │
│ 5. Search & Filter                  │
│ 6. Sort Tasks                       │
│ 7. Exit                             │
└─────────────────────────────────────┘
```

### 📝 Adding Tasks with New Features

The enhanced task creation system allows you to build comprehensive, intelligent tasks with multiple attributes. When adding a new task through the "Add Task" menu option, you'll be guided through each feature:

#### 🎯 **Priority Levels**
Choose from three priority levels to organize your tasks by importance:
- **🔴 High** - Urgent tasks that need immediate attention
- **🟡 Medium** - Important tasks with moderate urgency
- **🟢 Low** - Tasks that can be completed when time permits

*Priority levels affect task sorting and help you focus on what matters most.*

#### 🏷️ **Tagging System**
Create custom tags to categorize and organize your tasks:
- **Multiple Tags**: Assign any number of tags to a single task
- **Custom Categories**: Create tags like `work`, `personal`, `urgent`, `project-alpha`, `meeting`, etc.
- **Flexible Organization**: Tags help you filter and group related tasks
- **Search Enhancement**: Tags are included in keyword searches

*Example Tags: `work`, `home`, `shopping`, `health`, `learning`, `bills`, `creative`*

#### ⏰ **Due Dates & Reminders**
Set specific deadlines and intelligent reminders:
- **Date & Time**: Specify exact due dates and times (e.g., "2025-12-25 14:30")
- **Flexible Formats**: Natural language support for date input
- **Reminder Scheduling**: Set advance reminders (15 min, 1 hour, 1 day before)
- **Visual Indicators**: Overdue tasks are clearly marked in the task list

*Due dates help you track deadlines and manage time-sensitive commitments.*

#### 🔄 **Recurring Tasks**
Automate repetitive tasks with powerful recurrence patterns:

**Available Patterns:**
- **📅 Daily**: Every day at the specified time
- **📆 Weekly**: Every week on the same day/time
- **🗓️ Monthly**: Every month on the same date/time
- **📋 Yearly**: Every year on the same date/time

**Smart Features:**
- **Auto-Rescheduling**: Completed recurring tasks automatically create the next occurrence
- **Skip Overdue**: If you miss a recurring task, it schedules the next upcoming date
- **Independent Tracking**: Each occurrence is tracked separately for completion
- **Perfect For**: Daily habits, weekly meetings, monthly bills, yearly events

**Example Use Cases:**
- `Daily standup meeting` - Every weekday at 9:00 AM
- `Weekly team sync` - Every Monday at 2:00 PM
- `Monthly rent payment` - 1st of every month
- `Annual insurance renewal` - Every year on your policy renewal date

#### 🎨 **Task Creation Workflow**

When you select "Add Task" from the main menu, the application will:

1. **📝 Task Title** - Enter a clear, descriptive title
2. **🎯 Priority** - Choose High/Medium/Low priority level
3. **🏷️ Tags** - Add one or more custom tags (comma-separated)
4. **⏰ Due Date** - Set deadline (optional, format: YYYY-MM-DD HH:MM)
5. **🔄 Recurrence** - Choose recurrence pattern (optional)
6. **✅ Confirm** - Review and save your task

#### 💡 **Pro Tips**

- **Descriptive Titles**: Use clear, action-oriented titles (e.g., "Review Q4 financial report" instead of "report")
- **Tag Strategy**: Develop a consistent tagging system for better organization
- **Realistic Due Dates**: Set achievable deadlines to avoid task overload
- **Strategic Priorities**: Reserve High priority for truly urgent items
- **Leverage Recurrence**: Convert repetitive manual tasks into automated recurring ones

#### 📊 **Task Display**

Once created, your tasks appear in the task list with:
- **Priority Indicators**: Color-coded priority badges (🔴🟡🟢)
- **Tag Display**: All assigned tags shown as colored chips
- **Due Status**: Clear "DUE: [date]" or "OVERDUE" indicators
- **Recurring Badge**: 🔄 icon for recurring tasks
- **Completion Status**: ✅ for completed, ◻️ for pending tasks

### Search & Filter Menu
```
SEARCH & FILTER MENU
1. Search by Keyword
2. Filter by Priority
3. Filter by Tag
4. Return to Main Menu
```

### Sorting Options
Tasks can be sorted by:
- Priority (High → Medium → Low)
- Title (Alphabetically A→Z)
- Due Date (Earliest → Latest)

## 🏗️ Architecture

The application follows a clean, layered architecture:

### 📊 **Domain Layer** (`src/domain/`)
Contains business entities and rules:
- `task.py`: Extended Task model with priority, tags, due dates, recurrence, and reminders
- `task_list.py`: Collection of tasks with search, filter, and sort operations
- `recurrence_rule.py`: Recurrence pattern implementation
- `reminder.py`: Reminder configuration and scheduling
- `errors.py`: Domain-specific exceptions

### ⚙️ **Services Layer** (`src/services/`)
Contains business logic:
- `task_service.py`: Orchestrates operations on tasks with validation
- `validation.py`: Input validation functions for all features
- `recurrence_service.py`: Handles recurrence pattern logic
- `reminder_service.py`: Manages notification scheduling

### 💻 **UI Layer** (`src/ui/`)
Console user interface:
- `cli.py`: Main CLI interface with advanced features
- `menu.py`: Enhanced menu system with search/filter/sort options
- `formatters.py`: Output formatting with priority indicators and tags

### 🧪 **Test Structure** (`tests/`)
Comprehensive testing coverage:
- `test_domain/`: Domain model tests with all new functionality
- `test_services/`: Service layer tests
- `test_integration/`: Integration tests for CLI and business flows

## 🧪 Testing

The application maintains >80% test coverage across all new features:

```bash
# Run all tests
uv run pytest

# Run tests with coverage report
uv run pytest --cov=src --cov-report=term-missing

# Run specific test files
uv run pytest tests/test_domain/
uv run pytest tests/test_services/
uv run pytest tests/test_integration/
```

### Test Coverage Includes
- ✅ Task creation with priority, tags, due dates
- ✅ Recurring task functionality
- ✅ Search, filter, and sort operations
- ✅ Reminder notifications
- ✅ UI workflow tests
- ✅ Error handling and validation

## 🛠️ Development

### Technology Stack
- **Language**: Python 3.13+
- **Testing**: Pytest with extensive test coverage
- **Code Quality**: Ruff (linter & formatter)
- **Dependency Management**: UV package manager
- **Scheduling**: Croniter for recurrence pattern processing

### Development Commands
```bash
# Format code
uv run ruff format src tests

# Lint code
uv run ruff check src tests

# Run type checking (if using mypy)
uv run mypy src
```

### Project Structure
```
EVOLUTION-OF-TODO/
├── src/                    # Source code
│   ├── domain/            # Domain models
│   ├── services/          # Business logic
│   ├── ui/                # Console UI
│   └── scheduler/         # Time-based operations
├── tests/                 # Test files
├── specs/                 # Feature specifications
│   └── 003-recurring-tasks-due-dates/ # Feature spec
├── pyproject.toml         # Project configuration
└── README.md              # This file
```

## 👥 Contributing

We welcome contributions to enhance the application! Here's how you can contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Ensure tests pass (`uv run pytest`)
5. Add tests for new functionality
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Code Quality Standards
- All functions should have type hints
- All public functions need docstrings
- Follow PEP 8 style guidelines (enforced by ruff)
- Maintain >80% test coverage
- Write descriptive commit messages

## 📈 Feature Roadmap

### Phase I (Current) ✅
- ✅ Core task management (CRUD operations)
- ✅ Task priorities (High/Medium/Low)
- ✅ Tagging system for categorization
- ✅ Due dates and time reminders
- ✅ Recurring tasks with auto-scheduling
- ✅ Search, filter, and sort functionality

### Phase II (Planned)
- Persistence layer (file-based or database)
- Enhanced UI with TUI (Text User Interface)
- User authentication
- Export/import functionality

## 🤝 Support

If you encounter any issues or have questions:
- Check the [existing issues](https://github.com/iamKhan79690/EVOLUTION-OF-TODO/issues)
- Create a new issue with detailed information
- Consider contributing a fix if you find a bug

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">Made with ❤️ for better task management</p>

<p align="center">
  <sub>Built with Python and passion | © 2025 EVOLUTION-OF-TODO</sub>
</p>