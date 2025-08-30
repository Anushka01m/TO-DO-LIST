# todo.py

from task import Task
from storage import load_tasks, save_tasks

def display_tasks(tasks, filter_tag=None, show_completed=None):
    filtered = tasks
    if filter_tag:
        filtered = [t for t in filtered if filter_tag in t.tags]
    if show_completed is not None:
        filtered = [t for t in filtered if t.completed == show_completed]

    if not filtered:
        print("📭 No matching tasks.")
        return

    print("\n📝 Your Tasks:")
    for i, t in enumerate(filtered, 1):
        status = "✅" if t.completed else "❌"
        print(f"{i}. {t.title} | Due: {t.due_date or 'N/A'} | Priority: {t.priority} | Tags: {', '.join(t.tags)} | {status}")

def add_task(tasks):
    title = input("Task title: ").strip()
    due = input("Due date (YYYY-MM-DD or leave blank): ").strip()
    priority = input("Priority (Low/Medium/High): ").strip().capitalize()
    tags = input("Tags (comma-separated): ").strip().split(",")
    tags = [tag.strip() for tag in tags if tag.strip()]
    tasks.append(Task(title, due or None, priority or "Medium", False, tags))
    print("✅ Task added.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: "))
        removed = tasks.pop(idx - 1)
        print(f"🗑️ Removed: {removed.title}")
    except (ValueError, IndexError):
        print("❌ Invalid selection.")

def update_task(tasks):
    display_tasks(tasks)
    try:
        idx = int(input("Enter task number to update: "))
        task = tasks[idx - 1]
        task.title = input(f"New title [{task.title}]: ") or task.title
        task.due_date = input(f"New due date [{task.due_date or 'N/A'}]: ") or task.due_date
        task.priority = input(f"New priority [{task.priority}]: ") or task.priority
        tags = input(f"New tags (comma-separated) [{', '.join(task.tags)}]: ")
        if tags:
            task.tags = [tag.strip() for tag in tags.split(",") if tag.strip()]
        print("🔄 Task updated.")
    except (ValueError, IndexError):
        print("❌ Invalid selection.")

def toggle_completion(tasks):
    display_tasks(tasks)
    try:
        idx = int(input("Enter task number to toggle completion: "))
        task = tasks[idx - 1]
        task.completed = not task.completed
        print(f"🔁 Task marked as {'complete' if task.completed else 'incomplete'}.")
    except (ValueError, IndexError):
        print("❌ Invalid selection.")

def search_tasks(tasks):
    keyword = input("Enter keyword to search: ").strip().lower()
    results = [t for t in tasks if keyword in t.title.lower()]
    display_tasks(results)

def filter_by_tag(tasks):
    tag = input("Enter tag to filter by: ").strip()
    display_tasks(tasks, filter_tag=tag)

def filter_by_completion(tasks):
    status = input("Show (complete/incomplete): ").strip().lower()
    if status == "complete":
        display_tasks(tasks, show_completed=True)
    elif status == "incomplete":
        display_tasks(tasks, show_completed=False)
    else:
        print("❌ Invalid status.")

def main():
    tasks = load_tasks()
    while True:
        print("\n📋 Menu:\n1. View All\n2. Add\n3. Delete\n4. Update\n5. Toggle Completion\n6. Search\n7. Filter by Tag\n8. Filter by Status\n9. Save & Exit")
        choice = input("Choose (1–9): ").strip()
        if choice == "1": display_tasks(tasks)
        elif choice == "2": add_task(tasks)
        elif choice == "3": delete_task(tasks)
        elif choice == "4": update_task(tasks)
        elif choice == "5": toggle_completion(tasks)
        elif choice == "6": search_tasks(tasks)
        elif choice == "7": filter_by_tag(tasks)
        elif choice == "8": filter_by_completion(tasks)
        elif choice == "9":
            save_tasks(tasks)
            print("💾 Saved. Goodbye!")
            break
        else:
            print("⚠️ Invalid option.")

if __name__ == "__main__":
    main()
