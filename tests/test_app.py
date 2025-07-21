import pytest
from task_cli import helpers
from tinydb import TinyDB, Query


@pytest.fixture
def create_task(tmp_path):
    # TMP Database
    db_path = tmp_path / "test_tasks.json"
    db = TinyDB(db_path)
    helpers.set_db(db)

    # Add Test Task Lifecycle
    helpers.add("TEST TASK", "TEST DESCRIPTION")
    task = db.all()[0]
    return db, task.doc_id

def test_add_task_successfully(create_task):
    db, task_id = create_task
    result = db.search(Query()["task"] == "TEST TASK")

    assert len(result) == 1
    assert result[0]["task"] == "TEST TASK"
    assert result[0]["description"] == "TEST DESCRIPTION"

def test_update_task_successfully(create_task):
    db, task_id = create_task

    helpers.update(task_id, "TEST TASK UPDATE", "TEST UPDATE DESCRIPTION")
    task = db.get(doc_id=task_id)

    assert task["task"] == "TEST TASK UPDATE"
    assert task["description"] == "TEST UPDATE DESCRIPTION"

def test_mark_in_progress_successfully(create_task):
    db, task_id = create_task

    helpers.mark_in_progress(task_id)
    task = db.get(doc_id=task_id)

    assert task["status"] == "IN PROGRESS"

def test_mark_done_successfully(create_task):
    db, task_id = create_task

    helpers.mark_done(task_id)
    task = db.get(doc_id=task_id)

    assert task["status"] == "DONE"


def test_list_tasks_successfully(create_task):
    db, task_id = create_task

    tasks = db.all()
    assert len(tasks) == 1

    todo = db.search(Query()["status"] == "TODO")
    assert len(todo) == 1

    helpers.mark_in_progress(task_id)
    in_progress = db.search(Query()["status"] == "IN PROGRESS")
    assert len(in_progress) == 1

    helpers.mark_done(task_id)
    done = db.search(Query()["status"] == "DONE")
    assert len(done) == 1

def test_remove_task_successfully(create_task):
    db, task_id = create_task

    helpers.remove(task_id)
    tasks = db.all()

    assert len(tasks) == 0