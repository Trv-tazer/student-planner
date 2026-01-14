import datetime
from typing import Optional

class Task:
    """
    Represents a single task in the Student Planner.
    """
    def __init__(
        self, 
        title: str, 
        subject: str, 
        due_date: Optional[str] = None, 
        priority: str = "Medium", 
        completed: bool = False
    ):
        """
        Initialize a Task.
        
        Args:
            title: Name of the task.
            subject: Subject or class the task belongs to.
            due_date: Due date in 'YYYY-MM-DD' format (optional).
            priority: 'Low', 'Medium', 'High', or 'Urgent'.
            completed: Whether the task is done.
        """
        self.title = title
        self.subject = subject
        self.due_date = (
            datetime.datetime.strptime(due_date, "%Y-%m-%d").date() 
            if due_date else None
        )
        self.priority = priority
        self.completed = completed

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True

    def set_due_date(self, due_date: str):
        """Set or update the due date."""
        self.due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()

    def set_priority(self, priority: str):
        """Update the priority level."""
        if priority not in ["Low", "Medium", "High", "Urgent"]:
            raise ValueError("Priority must be one of: Low, Medium, High, Urgent")
        self.priority = priority

    def to_dict(self):
        """Convert the task to a dictionary for JSON storage."""
        return {
            "title": self.title,
            "subject": self.subject,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "priority": self.priority,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data: dict):
        """Create a Task object from a dictionary."""
        return Task(
            title=data["title"],
            subject=data["subject"],
            due_date=data.get("due_date"),
            priority=data.get("priority", "Medium"),
            completed=data.get("completed", False)
        )
