from models.tasks import Task

def format_task(task: Task):
    status = "completed" if task['id'] else "pending"
    return f"{task['id']}\t\t{task['title']}\t\t{task['description']}\t\t{status}"