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

def 