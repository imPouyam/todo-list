from datetime import datetime
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def show_menu():
    print("\n--- TODO LIST ---")
    print("1) Add Task")
    print("2) Show Tasks")
    print("3) Remove Task")
    print("4) Edit Task")
    print("5) Exit")

tasks = []

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        clear()
        task_name = input("Enter new task: ")
        task = {
            "name": task_name,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        tasks.append(task)
        print("Task added!")
    
    elif choice == "2":
        clear()
        print("\nYour Tasks:")
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t['name']} (added: {t['created_at']})")

    elif choice == "3":
        clear()
        print("\nWhich task do you want to remove?")
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t['name']}")
        num = int(input("Task number: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            print("Task removed!")
        else:
            print("Invalid task number!")

    elif choice == "4":
        clear()
        print("\nWhich task do you want to edit?")
        for i,t in enumerate(tasks):
            print(f"{i+1}.{t['name']}")
        num = int(input("Task number: "))
        if 1 <= num <= len(tasks):
            new_name = str(input("Enter the new name for this task: "))
            tasks[num-1]['name'] = new_name
            print("Task edited!")
        else:
            print("Invalid task number!")

    elif choice == "5":
        clear()
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")