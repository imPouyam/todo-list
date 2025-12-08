from datetime import datetime
import os
import json


# ─────────────────────────────────────
# Utility Functions
# ─────────────────────────────────────

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def load_file():
    return json.load(open("tasks.json", "r")) if os.path.exists("tasks.json") else []


def save_file():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def priority_text(p):
    return {1: "High", 2: "Medium", 3: "Low"}.get(p, "Low")


def show_task(t, index=None):
    """Pretty print a task."""
    num = f"{index + 1}. " if index is not None else ""
    print(
        f"{num}{t['name']} - {t['status']}\n"
        f"   Priority: {priority_text(t['priority'])}\n"
        f"   Description: {t['description']}\n"
        f"   Last edited: {t['created_at']}\n"
    )


def show_all_tasks():
    clear()
    print("\nYour Tasks:")

    sorted_tasks = sorted(tasks, key=lambda x: (x["status"] == "Completed", x["priority"]))

    for i, t in enumerate(sorted_tasks):
        show_task(t, i)


def select_task():
    """Show list & return index of selected task or None."""
    print("\nSelect a task:")
    for i, t in enumerate(tasks):
        print(f"{i+1}. {t['name']}")

    try:
        num = int(input("Task number: "))
        return num - 1 if 0 <= num - 1 < len(tasks) else None
    except:
        return None


# ─────────────────────────────────────
# Menu Functions
# ─────────────────────────────────────

def add_task():
    clear()
    name = input("Enter task name: ")
    desc = input("Enter description: ")

    priority = input("Priority (1=High, 2=Medium, 3=Low): ")
    priority = int(priority) if priority in ["1", "2", "3"] else 3

    task = {
        "name": name,
        "description": desc,
        "priority": priority,
        "status": "Not completed",
        "created_at": now(),
    }

    tasks.append(task)
    save_file()
    clear()
    print("Task added!")


def remove_task():
    clear()
    idx = select_task()
    if idx is None:
        clear()
        print("Invalid selection!")
        return

    tasks.pop(idx)
    save_file()
    clear()
    print("Task removed!")


def edit_task():
    clear()
    idx = select_task()

    if idx is None:
        clear()
        print("Invalid selection!")
        return

    task = tasks[idx]

    clear()
    show_task(task)

    if task['status'] != 'Completed':
        if input("Mark as completed? (Y/N): ").lower() == 'y':
            task['status'] = 'Completed'
            task['created_at'] = now()

    if input("Edit name? (Y/N): ").lower() == 'y':
        task['name'] = input("New name: ")
        task['created_at'] = now()

    if task['status'] != 'Completed':
        if input("Change priority? (Y/N): ").lower() == 'y':
            p = input("Priority (1=High, 2=Medium, 3=Low): ")
            if p in ["1", "2", "3"]:
                task['priority'] = int(p)
                task['created_at'] = now()

    if input("Edit description? (Y/N): ").lower() == 'y':
        task['description'] = input("New description: ")
        task['created_at'] = now()

    save_file()
    clear()
    print("Task updated!")


def search_task():
    clear()
    keyword = input("Search keyword: ").lower()

    results = [
        (i, t) for i, t in enumerate(tasks)
        if keyword in t['name'].lower() or keyword in t['description'].lower()
    ]

    clear()
    if not results:
        print("No tasks found!")
        return

    print("\nSearch Results:\n")
    for i, t in results:
        show_task(t, i)


# ─────────────────────────────────────
# Menu Loop
# ─────────────────────────────────────

def show_menu():
    print("\n--- TODO LIST ---")
    print("1) Add Task")
    print("2) Show Tasks")
    print("3) Remove Task")
    print("4) Edit Task")
    print("5) Search Task")
    print("6) Exit")


tasks = load_file()

while True:
    input("\nPress Enter to continue")
    clear()
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1": add_task()
    elif choice == "2": show_all_tasks()
    elif choice == "3": remove_task()
    elif choice == "4": edit_task()
    elif choice == "5": search_task()
    elif choice == "6":
        clear()
        print("Goodbye!")
        break
    else:
        clear()
        print("Invalid choice!")
