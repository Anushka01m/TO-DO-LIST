# todo.py

from task import Task
from storage import load_tasks, save_tasks

def display_tasks(tasks):
    if not tasks:
        print("📭 No tasks available.")
        return
    print("\n📝 Your Tasks:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t.title} | Due: {t.due_date or 'N/A'} | Priority: {t.priority}")

def add_task(tasks):
    title = input("Task title: ").strip()
    due = input("Due date (YYYY-MM-DD or leave blank): ").strip()
    priority = input("Priority (Low/Medium/High): ").strip().capitalize()
    tasks.append(Task(title, due or None, priority or "Medium"))
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
        print("🔄 Task updated.")
    except (ValueError, IndexError):
        print("❌ Invalid selection.")

def main():
    tasks = load_tasks()
    while True:
        print("\n📋 Menu:\n1. View\n2. Add\n3. Delete\n4. Update\n5. Save & Exit")
        choice = input("Choose (1–5): ").strip()
        if choice == "1": display_tasks(tasks)
        elif choice == "2": add_task(tasks)
        elif choice == "3": delete_task(tasks)
        elif choice == "4": update_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("💾 Saved. Goodbye!")
            break
        else:
            print("⚠️ Invalid option.")

if __name__ == "__main__":
    main()

