""" Todo manager API with SQLite DB """

import sqlite3

db = sqlite3.connect("tasks.db", check_same_thread=False)
cur = db.cursor()

def row_to_dict(row):
    if row is None:
        return None
    else:
        return {
            "id": row[0],
            "todo": row[1],
            "urgent": bool(row[2])
        }

def close_db():
    # db.commit()
    db.close()

def list_tasks():
    # Perform listing
    query = "SELECT * FROM tasks"
    tasks = []

    # Tuples to list
    for row in cur.execute(query).fetchall():
        tasks.append(row_to_dict(row))
    
    return tasks

def get_task(task_id):
    # Perform search
    query = "SELECT * FROM tasks WHERE id = ?"
    row = cur.execute(query, (task_id, )).fetchone()
    return row_to_dict(row)

def ins_task(new_task, urgent):
    # Perform insertion
    query = "INSERT INTO tasks(todo, urgent) VALUES (?, ?)"
    cur.execute(query, (new_task, int(urgent)))
    
    # Retrieve the inserted task
    task_id = cur.lastrowid
    return get_task(task_id)

def del_task(task_id):
    # Retrieve the task to delete
    task = get_task(task_id)

    # Perform deletion
    query = "DELETE FROM tasks WHERE id = ?"
    cur.execute(query, (task_id, ))
    return task

def upd_task(task_id, todo, urgent):
    # Perform update
    query = "UPDATE tasks SET todo = ?, urgent = ? WHERE id = ?"
    cur.execute(query, (todo, int(urgent), task_id))

    # Retrieve the updated task
    return get_task(task_id)