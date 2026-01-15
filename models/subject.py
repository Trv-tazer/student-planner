from typing import Optional, List

class Subject:
    """
    Represents a Subject/Class in the Student Planner.
    Stores references to tasks by their titles instead of full Task objects.
    """
    def __init__(
        self, 
        name: str, 
        teacher: Optional[str] = None,
        color: Optional[str] = None
    ):
        self.name = name
        self.teacher = teacher
        self.color = color
        self.task_titles: List[str] = []  # store only titles

    def add_task_title(self, task_title: str):
        """Add a task reference by title."""
        if task_title not in self.task_titles:
            self.task_titles.append(task_title)

    def remove_task_title(self, task_title: str):
        """Remove a task reference by title."""
        if task_title in self.task_titles:
            self.task_titles.remove(task_title)

    def has_task(self, task_title: str) -> bool:
        """Check if a task is assigned to this subject."""
        return task_title in self.task_titles

    def list_task_titles(self) -> List[str]:
        """Return all task titles."""
        return self.task_titles.copy()

    def __str__(self):
        return f"{self.name} ({self.teacher})"
