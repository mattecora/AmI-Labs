""" Todo manager API """

tasks = []
filename = "task_list.txt"

def list_tasks():
    return sorted(tasks)

def ins_task(task):
    tasks.append(task)
    return True

def del_task(task):
    try:
        tasks.remove(task)
        return True
    except ValueError:
        return False

def del_all_tasks(sub):
    removed = []

    for task in tasks:
        if task.find(sub) != -1:
            removed.append(task)
            tasks.remove(task)
    
    return removed

def read_tasks():
    try:
        with open(filename, "r") as f:
            for line in f:
                tasks.append(line[:-1])
        return True
    except FileNotFoundError:
        return False

def write_tasks():
    with open(filename, "w") as f:
        for task in sorted(tasks):
            f.write(task + "\n")
    return True