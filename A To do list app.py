# A To do list app

import os

def display_menu():
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Save Tasks")
    print("5. Load Tasks")
    print("6. Exit")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task {task} added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list. Please recheck")
    else:
        print("To-Do List: ")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter a task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task {removed_task} deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print(f"Tasks saved to {filename}.")

def load_tasks(filename="tasks.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file]
        print(f"Tasks loaded from {filename}.")
        return []

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
        elif choice == "5":
            tasks = load_tasks()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
