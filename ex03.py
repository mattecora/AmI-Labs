tasks = []

while True:
    print("Insert the number corresponding to the action you want to perform:")

    print("\t1. insert a new task;")
    print("\t2. remove a task;")
    print("\t3. show all the tasks;")
    print("\t4. close the program.")

    try:
        ans = int(input("Your choice: "))
        if ans == 1:
            new_task = input("Insert the task to insert: ")
            tasks.append(new_task)
            print("Task inserted.")
        elif ans == 2:
            del_task = input("Insert the task to remove: ")
            try:
                tasks.remove(del_task)
                print("Task removed.")
            except ValueError:
                print("Task not present.")
        elif ans == 3:
            print("Inserted tasks:")
            for task in tasks:
                print(task)
        elif ans == 4:
            break
        else:
            print("Not a valid number!")
    except ValueError:
        print("Not a number!")
