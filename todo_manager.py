""" Todo manager API with SQLite DB """

import sqlite3

db = sqlite3.connect("tasks.db", check_same_thread=False)
cur = db.cursor()

def close_db():
    # db.commit()
    db.close()

def list_tasks():
    # Perform listing
    query = "SELECT * FROM tasks"
    tasks = []

    # Tuples to list
    for row in cur.execute(query).fetchall():
        tasks.append({
            "id": row[0],
            "todo": row[1],
            "urgent": bool(row[2])
        })
    
    return tasks

def ins_task(new_task, urgent):
    # Perform insertion
    query = "INSERT INTO tasks(todo, urgent) VALUES (?, ?)"
    cur.execute(query, (new_task, int(urgent)))
    return True

def del_task(task_id):
    # Perform deletion
    query = "DELETE FROM tasks WHERE id = ?"
    cur.execute(query, (task_id, ))
    return True