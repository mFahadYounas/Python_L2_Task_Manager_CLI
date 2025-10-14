from models.tasks import Task


def format_task(task: Task):
    status = "completed" if task["status"] else "pending"
    return f"{task['id']}\t\t{task['title']}\t\t{task['description']}\t\t{status}"


def search_task_idx(task_list: list[Task], task_id: str) -> int:
    for i in range(len(task_list)):
        if task_list[i]["id"] == task_id:
            return i

    return -1
