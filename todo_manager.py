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
        tasks.append(row[1])
    
    return tasks

def ins_task(task):
    # Perform insertion
    query = "INSERT INTO tasks(todo) VALUES (?)"
    cur.execute(query, (task, ))
    return True

def del_task(task):
    # Check if present
    query = "SELECT COUNT(*) FROM tasks WHERE todo = ?"
    res = cur.execute(query, (task, )).fetchone()
    if res[0] == 1:
        # Perform deletion
        query = "DELETE FROM tasks WHERE todo = ?"
        cur.execute(query, (task, ))
        return True
    else:
        return False

def del_all_tasks(sub):
    # Check matching rows
    removed = []
    query = "SELECT * FROM tasks WHERE todo LIKE ?"
    for row in cur.execute(query, ("%" + sub + "%", )).fetchall():
        removed.append(row[1])

    # Perform deletions
    query = "DELETE FROM tasks WHERE todo LIKE ?"
    cur.execute(query, ("%" + sub + "%", ))

    return removed
