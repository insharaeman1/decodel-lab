def task_manager():
    # Initialize an empty list to store tasks
    tasks = []

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            # Add a task to the list
            new_task = input("Enter the task (e.g., 'Finish Python assignment'): ")
            tasks.append(new_task)
            print(f"'{new_task}' has been added successfully!")

        elif choice == "2":
            # View all tasks using a print loop
            if not tasks:
                print("Your task list is currently empty.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        elif choice == "3":
            # Delete a task from the list
            if not tasks:
                print("Your task list is currently empty, nothing to delete.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

                try:
                    task_num = int(
                        input("Enter the task number you want to delete: ")
                    )
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(
                            task_num - 1
                        )  # remove using index (0-based)
                        print(f"'{removed_task}' has been deleted successfully!")
                    else:
                        print("Invalid task number! Please try again.")
                except ValueError:
                    print(
                        "Please enter a valid number corresponding to the task."
                    )

        elif choice == "4":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")


# Run the program
if __name__ == "__main__":
    task_manager()