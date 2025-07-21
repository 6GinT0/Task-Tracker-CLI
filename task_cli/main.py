import sys
from . import helpers

def main():
    command = sys.argv[1]
    args = sys.argv[2:]

    commands = {
        "add": helpers.add,
        "update": helpers.update,
        "remove": helpers.remove,
        "mark-in-progress": helpers.mark_in_progress,
        "mark-done": helpers.mark_done,
        "list": helpers.list_tasks,
    }

    commands[command](*args)

if __name__ == "__main__":
    main()