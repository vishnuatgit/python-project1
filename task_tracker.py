import json
import os

# This is the name of the file where we will save our tasks.
# It will be created in the same folder as this script.
FILE_NAME = 'tasks.json'

def load_tasks():
    """
    This function reads the JSON file and converts it into a Python Dictionary.
    If the file doesn't exist yet, it returns an empty dictionary.
    """
    if not os.path.exists(FILE_NAME):
        # File doesn't exist yet, return an empty dictionary to start fresh.
        return {}
    
    # Open the file in 'r' (read) mode.
    try:
        with open(FILE_NAME, 'r') as file:
            # json.load() takes the text in the file and turns it into a Python dictionary!
            tasks = json.load(file)
            return tasks
    except json.JSONDecodeError:
        print("Warning: tasks.json is corrupted or empty. Starting fresh.")
        return {}

def save_tasks(tasks_dict):
    """
    This function takes our Python Dictionary and saves it to the JSON file.
    """
    # Open the file in 'w' (write) mode.
    with open(FILE_NAME, 'w') as file:
        # json.dump() converts the Python dictionary into a JSON string and writes it to the file.
        # indent=4 makes the JSON file readable for humans (adds spaces/tabs).
        json.dump(tasks_dict, file, indent=4)

def display_menu():
    print("\n--- CLI Task Tracker ---")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Delete a Task")
    print("4. Update a Task")
    print("5. Exit")

def main():
    # 1. When the program starts, load any existing tasks from the file.
    # 'tasks' is a Python Dictionary. Example: {"1": "Buy groceries", "2": "Read Python book"}
    tasks = load_tasks()
    
    # We need a counter to give each new task a unique ID (like "1", "2", "3")
    # If the dictionary has items, we find the highest ID. If it's empty, we start at 1.
    if tasks:
        # Get all the keys (which are strings), convert them to integers, and find the max.
        task_id_counter = max([int(key) for key in tasks.keys()]) + 1
    else:
        task_id_counter = 1

    # The main loop of the application. It runs forever until the user types '4' (Exit).
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("\n--- Your Tasks ---")
            if not tasks:
                print("You have no tasks! Enjoy your day.")
            else:
                # Loop through the dictionary and print the ID and the Task Description
                for task_id, task_desc in tasks.items():
                    print(f"[{task_id}] {task_desc}")

        elif choice == '2':
            new_task = input("\nEnter the new task: ")
            # Add the new task to the dictionary. We convert the counter to a string.
            tasks[str(task_id_counter)] = new_task
            print(f"Added task: '{new_task}'")
            
            # Save the updated dictionary to the file
            save_tasks(tasks)
            
            # Increment the counter for the next task
            task_id_counter += 1

        elif choice == '3':
            delete_id = input("\nEnter the ID of the task to delete: ")
            # Check if the ID exists in our dictionary
            if delete_id in tasks:
                removed_task = tasks.pop(delete_id) # .pop() removes the item from the dictionary
                print(f"Deleted task: '{removed_task}'")
                # Save the updated dictionary to the file
                save_tasks(tasks)
            else:
                print("Error: Task ID not found.")

        elif choice == '4':
            update_id = input("\nEnter the ID of the task to update: ")
            if update_id in tasks:
                print(f"Current task: '{tasks[update_id]}'")
                new_desc = input("Enter the new task description: ")
                tasks[update_id] = new_desc
                print(f"Updated task [{update_id}] to: '{new_desc}'")
                save_tasks(tasks)
            else:
                print("Error: Task ID not found.")

        elif choice == '5':
            print("\nSaving tasks and exiting. Goodbye!")
            break # This breaks us out of the 'while True' loop, ending the program.

        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

# This is a standard Python practice. It means "if this script is run directly, start the main() function"
if __name__ == "__main__":
    main()
