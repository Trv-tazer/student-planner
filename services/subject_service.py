from typing import List, Optional
from models.subject import Subject
from models.task import Task
from storage.file_storage import load_tasks, save_tasks  # for task lookup
import json
from pathlib import Path

DATA_FILE = Path("subjects.json")

class SubjectService:
    """
    Handles logic for managing subjects/classes.
    Stores only task titles; tasks are retrieved via TaskService.
    """
    def __init__(self):
        self.subjects: List[Subject] = self.load_subjects()

    # ---------- Subject Management ----------

    def add_subject(self, subject: Subject):
        """Add a new subject."""
        self.subjects.append(subject)
        self.save_subjects()

    def delete_subject(self, subject_name: str):
        """Delete a subject by name."""
        self.subjects = [s for s in self.subjects if s.name != subject_name]
        self.save_subjects()

    def get_subject(self, subject_name: str) -> Optional[Subject]:
        """Retrieve a subject by name."""
        for subject in self.subjects:
            if subject.name == subject_name:
                return subject
        return None

    def list_subjects(self) -> List[Subject]:
        """Return all subjects."""
        return self.subjects

    # ---------- Task Assignment ----------

    def assign_task_to_subject(self, subject_name: str, task_title: str):
        """Assign an existing task to a subject by title."""
        subject = self.get_subject(subject_name)
        if subject:
            subject.add_task_title(task_title)
            self.save_subjects()

    def remove_task_from_subject(self, subject_name: str, task_title: str):
        """Remove a task reference from a subject by title."""
        subject = self.get_subject(subject_name)
        if subject:
            subject.remove_task_title(task_title)
            self.save_subjects()

    def list_tasks_for_subject(self, subject_name: str, all_tasks: List[Task]) -> List[Task]:
        """
        Return Task objects assigned to a subject.
        all_tasks should come from TaskService.tasks
        """
        subject = self.get_subject(subject_name)
        if not subject:
            return []

        # Match task titles to Task objects
        return [t for t in all_tasks if t.title in subject.list_task_titles()]

    # ---------- Persistence ----------

    def save_subjects(self):
        """Persist subjects (with task titles only) to JSON."""
        data = []
        for s in self.subjects:
            data.append({
                "name": s.name,
                "teacher": s.teacher,
                "color": s.color,
                "task_titles": s.list_task_titles()
            })

        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def load_subjects(self) -> List[Subject]:
        """Load subjects from JSON."""
        if not DATA_FILE.exists():
            return []

        with open(DATA_FILE, "r") as f:
            data = json.load(f)

        subjects = []
        for item in data:
            subject = Subject(
                name=item["name"],
                teacher=item.get("teacher"),
                color=item.get("color")
            )
            for task_title in item.get("task_titles", []):
                subject.add_task_title(task_title)
            subjects.append(subject)

        return subjects
