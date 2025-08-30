# task.py

class Task:
    def __init__(self, title, due_date=None, priority="Medium", completed=False, tags=None):
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.completed = completed
        self.tags = tags or []

    def to_dict(self):
        return {
            "title": self.title,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed,
            "tags": self.tags
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["title"],
            data.get("due_date"),
            data.get("priority", "Medium"),
            data.get("completed", False),
            data.get("tags", [])
        )
