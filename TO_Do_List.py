tasks = [] # creates an empty list

def addTask(tasks):
    """
    Add Task Function:
    Asks the user which task to add.
    Adds the task to the list.
    Prints that the task has been successfully added to the list.
    """
    task = input("Please enter task you would like to add: ")
    tasks.append(task)
    print(f"Task '{task}' has been successfully added to the list.")

def listTasks(tasks):
    """
    List Tasks Function:
    Lists all tasks currently in the tasks list.
    """
    if not tasks:
        print("There are no tasks currently")
    else:
        print("Here are the tasks")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask(tasks):
    """
    Delete Task Function:
    Lists all tasks and prompts the user to enter the number of the task to delete.
    Deletes the specified task from the list.
    """
    listTasks(tasks)
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if 0 <= taskToDelete < len(tasks):
            del tasks[taskToDelete]
            print(f"Task #{taskToDelete} has been removed")
        else:
            print(f"Task #{taskToDelete} was not found")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    # Create a loop to run the app
    username = input("Hi, Welcome to the TO DO LIST APP!!\nThis app allows you to organize tasks, manage time, and prioritize activities.\nPlease enter your name: ")
    print(f"Welcome again {username} :)")
    while True:
        print("\n")
        print("Please select one of the following options below ***")
        print("__________________________________________")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            addTask(tasks)
        elif choice == "2":
            deleteTask(tasks)
        elif choice == "3":
            listTasks(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid input. Please try again.")
    print(f"Goodbye {username} :) ")