""" Todo manager API """

tasks = []

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
