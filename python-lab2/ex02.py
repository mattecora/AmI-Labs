from sys import argv

tasks = []

try:
    filename = argv[1]
    print("Filename is {}".format(filename))
except IndexError:
    print("No file provided on the command line!")
    exit()

try:
    with open(filename, "r") as f:
        for line in f:
            tasks.append(line[:-1])
except FileNotFoundError:
    print("The provided file does not exist. No task will be imported.")

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
            for task in sorted(tasks):
                print(task)
        elif ans == 4:
            break
        else:
            print("Not a valid number!")
    except ValueError:
        print("Not a number!")

with open(filename, "w") as f:
    for task in sorted(tasks):
        f.write(task + "\n")
