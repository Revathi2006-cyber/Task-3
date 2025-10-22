# Simple To-Do List (todo.py)

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added!\n")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter task number to remove: "))
            tasks.pop(num - 1)
            print("Task removed!\n")
        except:
            print("Invalid input!\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def main():
    tasks = load_tasks()

    while True:
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()