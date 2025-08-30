# storage.py

import json
from task import Task

FILE = "tasks.json"

def load_tasks():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
            return [Task.from_dict(d) for d in data]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)
