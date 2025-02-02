tasks = []

def add_task(task):
    tasks.append(task)

def view_tasks():
    for idx, task in enumerate(tasks):
        print(f"{idx + 1}. {task}")

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Quit")

    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        break
    else:
        print("Invalid choice")
