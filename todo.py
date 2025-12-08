from datetime import datetime
import os
import json

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def load_file():
    if os.path.exists("tasks.json"):
        with open("tasks.json" , "r")as file:
            return json.load(file)    
    return []    

def save_file():
    with open("tasks.json", "w")as file:
        json.dump(tasks, file, indent=4)

def priority_text(p):
    if p == 1:
        return "High"
    elif p == 2:
        return "Medium"
    else:
        return "Low"

def show_menu():
    print("\n--- TODO LIST ---")
    print("1) Add Task")
    print("2) Show Tasks")
    print("3) Remove Task")
    print("4) Edit Task")
    print("5) Search for Task")
    print("6) Exit")

tasks = load_file()

while True:
    wait = input("\nPress enter to continue")
    clear()
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        task_name = input("\nEnter new task: ")
        task_description = input("\nEnter a description for your task: ")
        priority = input("\nEnter priority (1=High, 2=Medium, 3=Low): ")
        if priority not in ["1", "2", "3"]:
            priority = "3"
        task = {
            "name": task_name,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "description": task_description,
            "priority": int(priority),
            "status": "Not completed"
        }
        tasks.append(task)
        save_file()
        clear()
        print("Task added!")
    
    elif choice == "2":
        clear()
        print("\nYour Tasks:")
        sorted_tasks = sorted(tasks, key=lambda x: (x["status"] == "Completed", x["priority"]))
        for i, t in enumerate(sorted_tasks):
            print(f"{i+1}. {t['name']} - {t['status']}\n   priority: {priority_text(t['priority'])}\n   Description: {t['description']} \n   last edited: {t['created_at']}\n")

    elif choice == "3":
        print("\nWhich task do you want to remove?")
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t['name']}")
        try:
            num = int(input("Task number: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num-1)
                save_file()
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
            print(f"{i+1}. {t['name']} - {t['status']}\n   Description: {t['description']}\n")
        try:
            num = int(input("Task number: "))
            if 1 <= num <= len(tasks):
                if (tasks[num-1]['status'] != 'Completed'):
                    if (input("Do you wish to change status? (Y/N)")).lower() == 'y':
                        tasks[num-1]['status'] = 'Completed'
                        tasks[num-1]['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if (input("Do you wish to change task name? (Y/N)")).lower() == 'y':
                    new_name = input("Enter the new name for this task: ")
                    tasks[num-1]['name'] = new_name
                    tasks[num-1]['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if (tasks[num-1]['status'] != 'Completed'):
                    if (input("Do you wish to change the priority? (Y/N)")).lower() == 'y':
                        new_priority = input("Enter new priority (1=High, 2=Medium, 3=Low): ")
                        if new_priority in ["1", "2", "3"]:
                            tasks[num-1]['priority'] = int(new_priority)
                            tasks[num-1]['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if (input("Do you wish to change the description? (Y/N)")).lower() == 'y':
                    new_description = input("Enter the new description for this task: ")
                    tasks[num-1]['description'] = new_description
                    tasks[num-1]['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")                                    
                save_file()
                clear()
                print("Task edited!")
            else:
                clear()
                print("Invalid task number!")
        except ValueError:
            clear()
            print("Invalid input! Please enter a number.")
            
    elif choice == "5":
        KeyWord = input("Enter keyword to search: ").lower()
        result = [] 
        for i, t in enumerate(tasks):
            if KeyWord in t['name'].lower() or KeyWord in t['description'].lower():
                result.append((i,t))
        clear()
        if result:
            print("\n Search Results: ")
            for i, t in result:
                print(f"{i+1}. {t['name']} - {t['status']}\n   Description: {t['description']} \n   last edited: {t['created_at']}\n")
        else:
            print("\nNo tasks found with that keyword!")
   
    elif choice == "6":
        clear()
        print("\nGoodbye!")
        break

    else:
        clear()
        print("Invalid choice!")