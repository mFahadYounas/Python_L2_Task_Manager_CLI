from models.tasks import Task
import os


def format_task(task: Task):
    status = "completed" if task["status"] else "pending"
    return f"{task['id']}\t\t{task['title']}\t\t{task['description']}\t\t{status}"


def search_task_idx(task_list: list[Task], task_id: str) -> int:
    for i in range(len(task_list)):
        if task_list[i]["id"] == task_id:
            return i

    return -1


def create_logs_dir():
    if not os.path.exists("logs/"):
        directory_name = "logs"
        try:
            os.mkdir(directory_name)
            print(f"Directory '{directory_name}' created successfully.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{directory_name}'.")
        except Exception as e:
            print(f"An error occurred: {e}")
