from typing import Optional, List
from models.task import Task

class Subject:
    """
    Represents a Subject/Class in the Student Planner.
    """
    def __init__(
        self, 
        name: str, 
        teacher: Optional[str] = None, 
        color: Optional[str] = None
    ):
        """
        Initialize a Subject.

        Args:
            name: Name of the subject/class.
            teacher: Optional teacher name.
            color: Optional color code for UI purposes.
        """
        self.name = name
        self.teacher = teacher
        self.color = color
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Add a task to this subject."""
        self.tasks.append(task)

    def remove_task(self, task_title: str):
        """Remove a task from this subject by title."""
        self.tasks = [t for t in self.tasks if t.title != task_title]

    def get_task(self, task_title: str) -> Optional[Task]:
        """Retrieve a task by title."""
        for t in self.tasks:
            if t.title == task_title:
                return t
        return None

    def list_tasks(self, sort_by: str = "priority") -> List[Task]:
        """Return tasks optionally sorted by priority or due date."""
        tasks = self.tasks.copy()
        if sort_by == "priority":
            priority_order = {"Urgent": 0, "High": 1, "Medium": 2, "Low": 3}
            tasks.sort(key=lambda x: priority_order.get(x.priority, 4))
        elif sort_by == "due_date":
            tasks.sort(key=lambda x: x.due_date or "9999-12-31")
        return tasks

    def __str__(self):
        return f"{self.name} ({self.teacher})"
