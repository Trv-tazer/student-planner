from services.task_service import TaskService
from services.subject_service import SubjectService
from models.task import Task
from models.subject import Subject

class CLI:
    """
    Command-line interface for the Student Planner.
    """
    def __init__(self):
        self.task_service = TaskService()
        self.subject_service = SubjectService()

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose an option: ").strip().lower()

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
            elif choice == "6":
                self.subject_menu()
            elif choice == "q":
                print("Exiting planner. Goodbye!")
                break
            else:
                print("Invalid choice.")

    def show_menu(self):
        print("\n--- STUDENT PLANNER ---")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Mark Task Complete")
        print("5. List Tasks")
        print("6. Manage Subjects")
        print("Q. Quit")

    # -------- TASKS --------

    def add_task(self):
        title = input("Task title: ").strip()
        subject = input("Subject/Class: ").strip()
        due_date = input("Due date (YYYY-MM-DD, optional): ").strip() or None
        priority = input("Priority (Low, Medium, High, Urgent): ").strip() or "Medium"

        task = Task(title, subject, due_date, priority)
        self.task_service.add_task(task)
        print("Task added.")

    def edit_task(self):
        title = input("Task to edit: ").strip()
        new_title = input("New title (blank to skip): ").strip() or None
        new_subject = input("New subject (blank to skip): ").strip() or None
        new_due_date = input("New due date (YYYY-MM-DD, blank to skip): ").strip() or None
        new_priority = input("New priority (blank to skip): ").strip() or None

        if self.task_service.edit_task(title, new_title, new_subject, new_due_date, new_priority):
            print("Task updated.")
        else:
            print("Task not found.")

    def delete_task(self):
        title = input("Task to delete: ").strip()
        self.task_service.delete_task(title)
        print("Task deleted (if it existed).")

    def mark_complete(self):
        title = input("Task to mark complete: ").strip()
        self.task_service.mark_complete(title)
        print("Task marked complete (if it existed).")

    def list_tasks(self):
        tasks = self.task_service.list_tasks()
        if not tasks:
            print("No tasks found.")
            return

        print("\n--- TASKS ---")
        for t in tasks:
            status = "✓" if t.completed else "✗"
            due = t.due_date.isoformat() if t.due_date else "No due date"
            print(f"[{status}] {t.title} | {t.subject} | {t.priority} | Due: {due}")

    # -------- SUBJECTS --------

    def subject_menu(self):
        print("\n--- SUBJECT MANAGEMENT ---")
        print("1. Add Subject")
        print("2. Delete Subject")
        print("3. List Subjects")
        print("4. Assign Task to Subject")
        print("B. Back")

        choice = input("Choose an option: ").strip().lower()

        if choice == "1":
            self.add_subject()
        elif choice == "2":
            self.delete_subject()
        elif choice == "3":
            self.list_subjects()
        elif choice == "4":
            self.assign_task_to_subject()

    def add_subject(self):
        name = input("Subject name: ").strip()
        teacher = input("Teacher (optional): ").strip() or None
        subject = Subject(name, teacher)
        self.subject_service.add_subject(subject)
        print("Subject added.")

    def delete_subject(self):
        name = input("Subject name to delete: ").strip()
        self.subject_service.delete_subject(name)
        print("Subject deleted (if it existed).")

    def list_subjects(self):
        subjects = self.subject_service.list_subjects()
        if not subjects:
            print("No subjects found.")
            return

        print("\n--- SUBJECTS ---")
        for s in subjects:
            print(f"- {s.name} ({len(s.tasks)} tasks)")

    def assign_task_to_subject(self):
        task_title = input("Task title: ").strip()
        subject_name = input("Subject name: ").strip()

        task = self.task_service.get_task(task_title)
        if not task:
            print("Task not found.")
            return

        self.subject_service.assign_task_to_subject(subject_name, task)
        print("Task assigned to subject.")

