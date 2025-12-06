from datetime import datetime

def show_menu():
    print("\n--- TODO LIST ---")
    print("1) Add Task")
    print("2) Show Tasks")
    print("3) Remove Task")
    print("4) Exit")

tasks = []

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        task_name = input("Enter new task: ")
        task = {
            "name": task_name,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        tasks.append(task)
        print("Task added!")
    
    elif choice == "2":
        print("\nYour Tasks:")
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t['name']} (added: {t['created_at']})")

    elif choice == "3":
        print("\nWhich task do you want to remove?")
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t}")
        num = int(input("Task number: "))
        tasks.pop(num-1)
        print("Task removed!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")