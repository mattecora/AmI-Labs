tasks = {
    "task1": {"todo": "call John for AmI project organization", "urgent": True},
    "task2": {"todo": "buy a new mouse", "urgent": True},
    "task3": {"todo": "find a present for Angelina's birthday", "urgent": False},
    "task4": {"todo": "organize mega party (last week of April)", "urgent": False},
    "taks5": {"todo": "book summer holidays", "urgent": False},
    "task6": {"todo": "whatsapp Mary for a coffee", "urgent": False}
}

urg_tasks = {}

for task_name in tasks:
    if tasks[task_name]["urgent"]:
        urg_tasks[task_name] = tasks[task_name]

print("Your urgent tasks are:")
for task in urg_tasks.values():
    print(task["todo"])
