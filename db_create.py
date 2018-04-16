import sqlite3

# Open DB
db = sqlite3.connect("prova.db")
cur = db.cursor()

# Create table
cur.execute("CREATE TABLE tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, todo VARCHAR(200))")

# Read tasks and DB insert
tasks = []
try:
    with open("task_list.txt", "r") as f:
        for line in f:
            cur.execute("INSERT INTO tasks(todo) VALUES (?)", (line[:-1], ))
except FileNotFoundError:
    print("Error in opening file. No task will be imported.")

# Print tasks
print(cur.execute("SELECT * FROM tasks").fetchall())

# Close DB
db.close()