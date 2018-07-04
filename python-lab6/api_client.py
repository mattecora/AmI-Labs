from requests import get, post, put, delete

base_uri = "http://127.0.0.1:5000/tasks"

def pretty_print_task(task):
    print("-" * 20 + " Task #{} ".format(task["id"]) + "-" * 20)
    print("Todo:\t{}".format(task["todo"]))
    print("Urgent:\t{}".format(task["urgent"]))
    print("-" * len("-" * 20 + " Task #{} ".format(task["id"]) + "-" * 20))

def list_tasks():
    req = get(base_uri)
    if req.status_code == 200:
        print("Inserted tasks:")
        for task in req.json():
            pretty_print_task(task)
    else:
        print("Server returned a {} error.".format(req.status_code))

def add_task():
    todo = input("Insert the new task: ")
    urgent = input("Is the task urgent (yes)? ") == "yes"
    req = post(base_uri, json={
        "todo": todo,
        "urgent": urgent
    })
    if req.status_code == 200:
        print("Your task was successfully inserted!")
        pretty_print_task(req.json())
    else:
        print("Server returned a {} error.".format(req.status_code))

def get_task():
    try:
        task_id = int(input("What is the ID of the task? "))
        req = get(base_uri + "/{}".format(task_id))
        if req.status_code == 200:
            pretty_print_task(req.json())
        else:
            print("Server returned a {} error.".format(req.status_code))
    except ValueError:
        print("Not a valid number!")

def upd_task():
    try:
        task_id = int(input("What is the ID of the task? "))
        todo = input("Insert the updated task: ")
        urgent = input("Is the task urgent (yes)? ") == "yes"
        req = put(base_uri + "/{}".format(task_id), json={
            "task_id": task_id,
            "todo": todo,
            "urgent": urgent
        })
        if req.status_code == 200:
            print("Your task was successfully updated!")
            pretty_print_task(req.json())
        else:
            print("Server returned a {} error.".format(req.status_code))
    except ValueError:
        print("Not a valid number!")

def del_task():
    try:
        task_id = int(input("What is the ID of the task? "))
        req = delete(base_uri + "/{}".format(task_id))
        if req.status_code == 200:
            print("Your task was successfully deleted!")
            pretty_print_task(req.json())
        else:
            print("Server returned a {} error.".format(req.status_code))
    except ValueError:
        print("Not a valid number!")

if __name__ == "__main__":
    print("Welcome to the Todo List Manager!")
    while True:
        print("Insert the number corresponding to the action you want to perform:")
        print("\t1. list all the tasks")
        print("\t2. add a task")
        print("\t3. retrieve a single task")
        print("\t4. update a task")
        print("\t5. delete a task")
        print("\t6. exit")

        try:
            ans = int(input("Your choice: "))
            if ans == 1:
                list_tasks()
            elif ans == 2:
                add_task()
            elif ans == 3:
                get_task()
            elif ans == 4:
                upd_task()
            elif ans == 5:
                del_task()
            elif ans == 6:
                break
            else:
                print("Not a valid number!")
        except ValueError:
            print("Not a number!")