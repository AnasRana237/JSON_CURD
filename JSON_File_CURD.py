import json

def view_all_tasks():
    with open("task.json", "r") as f:
        dict1 =  f.read()
    print(dict1)

def add_task(title, status):
    task = []
    with open("task.json", "r", encoding="utf-8") as f:
        task = json.load(f)
    task.append({"title": title, "status": status})
    with open("task.json", "w") as f:
        json.dump(task, f, indent=4, ensure_ascii=False)
    print(f"Task '{title}' added successfully!")

def mark(title,status):

    with open("task.json", "r") as f:
        tasks = json.load(f)

    for task in tasks:
        if task.get("title") == title:
            task["status"]= status
            break

    with open("task.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)


    print(f"Task '{title}' updated to status '{status}'.")

def delete_task(title):

    with open("task.json", "r") as f:
        tasks = json.load(f)

    for task in tasks:
        if task.get("title") == title:
            tasks.remove(task)
            break

    with open("task.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)


    print(f"Task '{title}' Successfully Delete.")

def search_task(title):

    with open("task.json", "r") as f:
        tasks = json.load(f)

    for task in tasks:
        if task.get("title") == title:
            print(f" {task['title']} - {task['status']}")
            break

def main():
    while True:
        print("\n--- Task Manager ---")
        print("1. View all tasks")
        print("2. Add a new task")
        print("3. Mark task as complete / change status")
        print("4. Delete a task")
        print("5. Search a task")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            view_all_tasks()
        elif choice == "2":
            title = input("Enter task title: ")
            status = input("Enter task status (Pending/Completed): ")
            add_task(title, status)
        elif choice == "3":
            title = input("Enter task title to update: ")
            status = input("Enter new status: ")
            mark(title, status)
        elif choice == "4":
            title = input("Enter task title to delete: ")
            delete_task(title)
        elif choice == "5":
            title = input("Enter task title to search: ")
            search_task(title)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()