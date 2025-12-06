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
    wait = input("\nPress enter to continue")
    clear()
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        task_name = input("\nEnter new task: ")
        task = {
            "name": task_name,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        tasks.append(task)
        clear()
        print("Task added!")
    
    elif choice == "2":
        clear()
        print("\nYour Tasks:")
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t['name']} (last edited: {t['created_at']})")

    elif choice == "3":
        print("\nWhich task do you want to remove?")
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t['name']}")
        try:
            num = int(input("Task number: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num-1)
                clear()
                print("Task removed!")
            else:
                clear()
                print("Invalid task number!")
        except ValueError:
            clear()
            print("Invalid input! Please enter a number.")        

    elif choice == "4":
        print("\nWhich task do you want to edit?")
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t['name']}")
        try:
            num = int(input("Task number: "))
            if 1 <= num <= len(tasks):
                new_name = input("Enter the new name for this task: ")
                tasks[num-1]['name'] = new_name
                tasks[num-1]['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                clear()
                print("Task edited!")
            else:
                clear()
                print("Invalid task number!")
        except ValueError:
            clear()
            print("Invalid input! Please enter a number.")

    elif choice == "5":
        clear()
        print("\nGoodbye!")
        break

    else:
        clear()
        print("Invalid choice!")