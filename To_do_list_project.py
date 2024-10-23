class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False
    def mark_complete(self):
        self.completed = True
    def __str__(self):
        status = "completed" if self.completed else "incomplete"
        return f"{self.title} - {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print(f"task '{title}' added.")
    def view_tasks(self):
        if not self.tasks:
            print("no tasks available")
            return
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")
    def mark_task_complete(self, index):
        try:
            self.tasks[index].mark_complete()
            print(f"task '{self.tasks[index].title}' marked as complete")
        except IndexError:
            print("invalid task number")
    def delete_task(self, index):
        try:
            remove_task = self.tasks.pop(index)
            print(f"task '{remove_task.title}' deleted")
        except IndexError:
            print("invalid task number")
    def display_menu(self):
        print("\nWelcome to the To-Do List App!")
        print("\nMenu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Quit")
def main():
    todo_list = ToDoList()
    while True:
        todo_list.display_menu()
        choice = input("Select an option (1-5): ")
        try:
            if choice == '1':
                title = input("Enter the task title: ")
                todo_list.add_task(title)
            elif choice == '2':
                todo_list.view_tasks()
            elif choice == '3':
                task_number = int(input("Enter the task number to mark as complete: ")) - 1
                todo_list.mark_task_complete(task_number)
            elif choice == '4':
                task_number = int(input("Enter the task number to delete: ")) - 1
                todo_list.delete_task(task_number)
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")  
if __name__ == "__main__":
    main()