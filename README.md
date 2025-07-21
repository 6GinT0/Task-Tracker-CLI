# Task CLI

CLI for managing tasks (https://roadmap.sh/projects/task-tracker)

---

## Requirements

- Python 3.8 o superior

---

## Instalation

1. Clone the repository:
   ```bash
   git clone https://github.com/tu_usuario/task-cli.git
   cd Task-Tracker-CLI
   ```
2. Create and activate a virtual environment
  * Linux/macOS:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
  * Windows (cmd):
    ```bash
    python -m venv venv
    venv\Scripts\activate.bat
    ```
  * Windows (PowerShell):
    ```bash
    python -m venv venv
    venv\Scripts\Activate.ps1
    ```
3. Install the project and its dependencies:
   ```bash
   pip install -e .
   ```
   Or if you want to include development dependencies:
   ```bash
   pip install -e .[dev]
   ```
## Usage

```bash
task-cli
```

---

## Commands

- `add <task> [description]` – Add task
- `update <id> <task> [description]` – Update task
- `remove <id>` – Remove task
- `mark-in-progress <id>` – Mark task in progress
- `mark-done <id>` – Mark task done
- `list [status]` – List tasks (todo, in-progress, done)

---

## Testing

```bash
pytest
```

---

## Licencia

MIT License

