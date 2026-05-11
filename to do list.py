from colorama import Fore, Style, init
import os

init()

tasks = []

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Add task
def add_task():
    task = input(Fore.GREEN + "Enter new task: " + Style.RESET_ALL)
    tasks.append(task)
    print(Fore.CYAN + "✅ Task added successfully!\n" + Style.RESET_ALL)

# View tasks
def view_tasks():
    if not tasks:
        print(Fore.RED + "📭 No tasks available.\n" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "\n Your Tasks:\n" + Style.RESET_ALL)
        for index, task in enumerate(tasks, start=1):
            print(Fore.BLUE + f"{index}. {task}" + Style.RESET_ALL)
        print()

# Delete task
def delete_task():
    view_tasks()

    if tasks:
        try:
            task_num = int(input(Fore.GREEN + "Enter task number to delete: " + Style.RESET_ALL))

            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(Fore.CYAN + f" '{removed}' deleted successfully!\n" + Style.RESET_ALL)
            else:
                print(Fore.RED + "❌ Invalid task number!\n" + Style.RESET_ALL)

        except ValueError:
            print(Fore.RED + "❌ Please enter a valid number!\n" + Style.RESET_ALL)

# Main Program
while True:
    clear_screen()

    print(Fore.MAGENTA + "====== TO-DO LIST ======" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit" + Style.RESET_ALL)

    choice = input(Fore.GREEN + "\nEnter your choice: " + Style.RESET_ALL)

    if choice == '1':
        add_task()

    elif choice == '2':
        view_tasks()

    elif choice == '3':
        delete_task()

    elif choice == '4':
        print(Fore.CYAN + "\n👋 Exiting To-Do List..." + Style.RESET_ALL)
        break

    else:
        print(Fore.RED + "❌ Invalid choice!\n" + Style.RESET_ALL)

    input(Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)