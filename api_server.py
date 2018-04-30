from flask import Flask, request, jsonify
from todo_manager import close_db, list_tasks, get_task, ins_task, del_task, upd_task

app = Flask(__name__)
tasks = list_tasks()

@app.route("/tasks", methods=["GET"])
def handler_list_tasks():
    return jsonify(list_tasks())

@app.route("/tasks", methods=["POST"])
def handler_add_task():
    req_data = request.json
    return jsonify(ins_task(req_data["todo"], req_data["urgent"]))

@app.route("/tasks/<int:task_id>", methods=["GET"])
def handler_show_task(task_id):
    return jsonify(get_task(task_id))

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def handler_update_task(task_id):
    req_data = request.json
    return jsonify(upd_task(task_id, req_data["todo"], req_data["urgent"]))

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def handler_delete_task(task_id):
    return jsonify(del_task(task_id))

if __name__ == '__main__':
    app.run()
    close_db()