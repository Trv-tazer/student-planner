from services.task_service import TaskService

class CLI:
    """
    Command-line interface for the Student Planner.
    """
    def __init__(self):
        self.service = TaskService()

    def run(self):
        """
        Main loop for the CLI.
        """
        while True:
            self.show_menu()
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.edit_task()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                self.mark_complete()
            elif choice == "5":
                self.list_tasks()
            elif choice.lower() == "q":
                print("Exiting planner. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

    def show_menu(self):
        print("\n--- STUDENT PLANNER ---")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Mark Task Complete")
        print("5. List Tasks")
        print("Q. Quit")

    def add_task(self):
        title = input("Task title: ").strip()
        subject = input("Subject/Class: ").strip()
        due_date = input("Due date (YYYY-MM-DD, leave blank if none): ").strip() or None
        priority = input("Priority (Low, Medium, High, Urgent): ").strip() or "Medium"

        task = self.service.service.tasks.__class__(title, subject, due_date, priority) if False else None
        from models.task import Task
        task = Task(title=title, subject=subject, due_date=due_date, priority=priority)
        self.service.add_task(task)
        print(f"Task '{title}' added!")

    def edit_task(self):
        title = input("Task to edit: ").strip()
        new_title = input("New title (leave blank to keep same): ").strip() or None
        new_subject = input("New subject (leave blank to keep same): ").strip() or None
        new_due_date = input("New due date (YYYY-MM-DD, leave blank to keep same): ").strip() or None
        new_priority = input("New priority (Low, Medium, High, Urgent, leave blank to keep same): ").strip() or None

        if self.service.edit_task(title, new_title, new_subject, new_due_date, new_priority):
            print(f"Task '{title}' updated!")
        else:
            print(f"Task '{title}' not found.")

    def delete_task(self):
        title = input("Task to delete: ").strip()
        self.service.delete_task(title)
        print(f"Task '{title}' deleted (if it existed).")

    def mark_complete(self):
        title = input("Task to mark complete: ").strip()
        self.service.mark_complete(title)
        print(f"Task '{title}' marked complete (if it existed).")

    def list_tasks(self):
        sort_by = input("Sort by (priority/due_date): ").strip() or "priority"
        subject_filter = input("Filter by subject (leave blank for all): ").strip() or None

        tasks = self.service.list_tasks(sort_by=sort_by, subject_filter=subject_filter)
        if not tasks:
            print("No tasks found.")
            return

        print("\n--- TASK LIST ---")
        for t in tasks:
            status = "✓" if t.completed else "✗"
            due = t.due_date.isoformat() if t.due_date else "No due date"
            print(f"[{status}] {t.title} | {t.subject} | {t.priority} | Due: {due}")
