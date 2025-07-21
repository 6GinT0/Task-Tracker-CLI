from tinydb import TinyDB, Query
from datetime import datetime
from termcolor import colored

db = None

def set_db(database):
    global db
    db = database

def add(task, description = None):
    db.insert({
        "task": task,
        "description": description,
        "status": "TODO",
        "createdAt": str(datetime.now()),
        "updatedAt": str(datetime.now())
    })

    text = colored("Task added!", "green")
    print(text)

def update(id, task, description = None):
    doc = db.get(doc_id=id)

    db.update({
        "task": task,
        "description": description if description else doc["description"],
        "updatedAt": str(datetime.now())
    }, doc_ids=[int(id)])

    text = colored("Task updated!", "green")
    print(text)

def remove(id):
    db.remove(doc_ids=[int(id)])

    text = colored("Task deleted!", "green")
    print(text)

def mark_in_progress(id):
    db.update({
        "status": "IN PROGRESS",
        "updatedAt": str(datetime.now())
    }, doc_ids=[int(id)])

    text = colored("Mark as in progress!", "green")
    print(text)

def mark_done(id):
    db.update({
        "status": "DONE",
        "updatedAt": str(datetime.now())
    }, doc_ids=[int(id)])

    text = colored("Mark as done!", "green")
    print(text)


def list_tasks(status = None):
    actions = {
        None: list_all,
        "todo": list_todo,
        "in-progress": list_in_progress,
        "done": list_done,
    }

    actions[status]()

    return

def list_all():
    tasks = db.all()

    for task in tasks:
        print(f"{task.doc_id} - {task['task']} - {colored(task['status'], select_color(task['status']))}")

def list_todo():
    tasks = db.search(Query().status == "TODO")

    for task in tasks:
        print(f"{task.doc_id} - {task['task']} - {colored(task['status'], "yellow")}")

def list_in_progress():
    tasks = db.search(Query().status == "IN PROGRESS")

    for task in tasks:
        print(f"{task.doc_id} - {task['task']} - {colored(task['status'], "blue")}")

def list_done():
    tasks = db.search(Query().status == "DONE")

    for task in tasks:
        print(f"{task.doc_id} - {task['task']} - {colored(task['status'], "green")}")

def select_color(status):
    colors = {
        "TODO": "yellow",
        "IN PROGRESS": "blue",
        "DONE": "green"
    }

    return colors[status]

if db is None:
    from pathlib import Path
    default_path = Path(__file__).parent / "tasks.json"
    set_db(TinyDB(default_path))