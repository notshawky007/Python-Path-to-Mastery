tasks = []  # This will hold all the tasks

# Function to add a task
def add_task():
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")
    task = {"title": title, "description": description, "completed": False}
    tasks.append(task)
    print(f"Task '{title}' has been added.")

# Function to delete a task
def delete_task():
    if not tasks:
        print("No tasks available to delete.")
        return
    view_tasks()  # Display tasks to choose from
    task_id = int(input("Enter the task number to delete: "))
    if 1 <= task_id <= len(tasks):
        removed_task = tasks.pop(task_id - 1)
        print(f"Task '{removed_task['title']}' has been deleted.")
    else:
        print("Invalid task number.")

# Function to edit a task
def edit_task():
    if not tasks:
        print("No tasks available to edit.")
        return
    view_tasks()  # Display tasks to choose from
    task_id = int(input("Enter the task number to edit: "))
    if 1 <= task_id <= len(tasks):
        new_title = input("Enter the new title: ")
        new_description = input("Enter the new description: ")
        tasks[task_id - 1]["title"] = new_title
        tasks[task_id - 1]["description"] = new_description
        print("Task has been updated.")
    else:
        print("Invalid task number.")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks to display.")
        return
    print("\nTasks List:")
    for idx, task in enumerate(tasks, 1):
        completed = "Completed" if task["completed"] else "Not Completed"
        print(f"{idx}. {task['title']} - {task['description']} ({completed})")

# Main menu function
def main_menu():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Edit Task")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            delete_task()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            view_tasks()
        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
