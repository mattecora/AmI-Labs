from flask import Flask, render_template, request, redirect
from todo_manager import close_db, list_tasks, ins_task, del_task

app = Flask(__name__)
tasks = list_tasks()

@app.route("/")
def index():
    return render_template("tasks.html", tasks=tasks)

@app.route("/insert_task", methods=["POST"])
def insert_task():
    global tasks
    new_task = request.form["new_task"]
    urgent = "urgent" in request.form
    ins_task(new_task, urgent)
    tasks = list_tasks()
    return redirect("/")

@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    global tasks
    del_task(task_id)
    tasks = list_tasks()
    return redirect("/")

if __name__ == '__main__':
    app.run()
    # close_db()