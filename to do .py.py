def show_menu():
    print("\nTo-Do List App")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark task as done")
    print("5. Exit")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    print("\nTasks:")
    for i, (task, done) in enumerate(tasks, 1):
        status = "✓" if done else " "
        print(f"{i}. [{status}] {task}")

def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append((task, False))
        print(f"Added task: {task}")
    else:
        print("Empty task not added.")

def remove_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Enter task number to remove: "))
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            print(f"Removed task: {removed[0]}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_done(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Enter task number to mark as done: "))
        if 1 <= idx <= len(tasks):
            task, _ = tasks[idx - 1]
            tasks[idx - 1] = (task, True)
            print(f"Marked task as done: {task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
