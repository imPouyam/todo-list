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
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t}")

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