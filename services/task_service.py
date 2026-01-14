from models.task import Task
from storage.file_storage import save_tasks, load_tasks
from typing import List, Optional

class TaskService:
    """
    Handles logic for adding, editing, deleting, and sorting tasks.
    """
    def __init__(self):
        # Load existing tasks from storage
        self.tasks: List[Task] = load_tasks()

    def add_task(self, task: Task):
        """Add a new task and save."""
        self.tasks.append(task)
        save_tasks(self.tasks)

    def delete_task(self, task_title: str):
        """Delete a task by its title."""
        self.tasks = [t for t in self.tasks if t.title != task_title]
        save_tasks(self.tasks)

    def get_task(self, task_title: str) -> Optional[Task]:
        """Retrieve a task by title."""
        for task in self.tasks:
            if task.title == task_title:
                return task
        return None

    def mark_complete(self, task_title: str):
        """Mark a task as completed."""
        task = self.get_task(task_title)
        if task:
            task.mark_complete()
            save_tasks(self.tasks)

    def edit_task(
        self, 
        task_title: str, 
        new_title: Optional[str] = None,
        new_subject: Optional[str] = None,
        new_due_date: Optional[str] = None,
        new_priority: Optional[str] = None
    ):
        """Edit task attributes."""
        task = self.get_task(task_title)
        if not task:
            return False

        if new_title:
            task.title = new_title
        if new_subject:
            task.subject = new_subject
        if new_due_date:
            task.set_due_date(new_due_date)
        if new_priority:
            task.set_priority(new_priority)

        save_tasks(self.tasks)
        return True

    def list_tasks(self, sort_by: str = "priority", subject_filter: Optional[str] = None):
        """
        Return tasks, optionally sorted and/or filtered by subject.
        sort_by options: 'priority' or 'due_date'
        """
        filtered = self.tasks
        if subject_filter:
            filtered = [t for t in filtered if t.subject == subject_filter]

        if sort_by == "priority":
            priority_order = {"Urgent": 0, "High": 1, "Medium": 2, "Low": 3}
            filtered.sort(key=lambda x: priority_order.get(x.priority, 4))
        elif sort_by == "due_date":
            filtered.sort(key=lambda x: x.due_date or "9999-12-31")  # tasks with no due date at the end

        return filtered
