from models.tasks import Task
from .utils import format_task, search_task_idx
from uuid import uuid4
from .decorators import log_info
import json


@log_info
def add_task() -> None:
    new_task: Task = {
        "id": str(uuid4()),
        "title": "",
        "description": "",
        "status": False,
    }

    new_task["title"] = input("Enter task title: ")
    new_task["description"] = input("Enter task description (optional): ")

    try:
        with open("storage/store.json", "r") as jf:
            data: list[Task] = json.load(jf)
            data.append(new_task)

        with open("storage/store.json", "w") as jf:
            json.dump(data, jf, indent=2)

    except FileNotFoundError:
        print("Storage file not found")


@log_info
def rem_task() -> None:
    task_id = input("Enter id of task to delete: ")

    try:
        with open("storage/store.json", "r") as jf:
            task_list: list[Task] = json.load(jf)
            task_idx = search_task_idx(task_list, task_id)
            if task_idx >= 0:
                task_list.pop(task_idx)
            else:
                print("Task with given ID does not exist!")

        with open("storage/store.json", "w") as jf:
            json.dump(task_list, jf, indent=2)

    except FileNotFoundError:
        print("Storage file not found")


@log_info
def toggle_task_status() -> None:
    task_id = input("Enter id of task to toggle status: ")

    try:
        with open("storage/store.json", "r") as jf:
            task_list: list[Task] = json.load(jf)
            task_idx = search_task_idx(task_list, task_id)
            if task_idx >= 0:
                task_list[task_idx]["status"] = not task_list[task_idx]["status"]
            else:
                print("Task with given ID does not exist!")

        with open("storage/store.json", "w") as jf:
            json.dump(task_list, jf, indent=2)

    except FileNotFoundError:
        print("Storage file not found")


@log_info
def view_all_tasks() -> None:
    print("ID\t\tTitle\t\tDescription\t\tStatus")
    try:
        with open("storage/store.json", "r") as jf:
            task_list: list[Task] = json.load(jf)
            for task in task_list:
                print(format_task(task))

    except FileNotFoundError:
        print("Storage file not found")


@log_info
def view_all_completed() -> None:
    print("ID\t\tTitle\t\tDescription\t\tStatus")
    try:
        with open("storage/store.json", "r") as jf:
            task_list: list[Task] = json.load(jf)
            for task in task_list:
                if task["status"]:
                    print(format_task(task))

    except FileNotFoundError:
        print("Storage file not found")


actions = {
    1: add_task,
    2: view_all_tasks,
    3: view_all_completed,
    4: toggle_task_status,
    5: toggle_task_status,
    6: rem_task,
}
