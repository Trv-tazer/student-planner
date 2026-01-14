import json
from pathlib import Path
from models.task import Task

DATA_FILE = Path("tasks.json")

def save_tasks(tasks):
    """
    Save a list of Task objects to a JSON file.
    """
    data = [task.to_dict() for task in tasks]
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_tasks():
    """
    Load tasks from the JSON file and return a list of Task objects.
    """
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        return [Task.from_dict(item) for item in data]
