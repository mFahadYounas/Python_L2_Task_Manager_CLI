from models.tasks import Task
import json

def search_task_idx(task_id: int) -> int:
    return task_id - 1

def add_task() -> None:
    new_task: Task = {
        "id": 0,
        "title": "",
        "description": "",
        "status": "pending"
    }

    new_task["title"]= input("Enter task title: ")
    new_task["description"] = input("Enter task description (optional): ")
    
    try:
        with open("storage/store.json", 'r') as jf:
            data: list[Task] = json.load(jf)
            new_task["id"] = len(data) + 1
            data.append(new_task)
        
        with open("storage/store.json", 'w') as jf:
            json.dump(data, jf, indent=2)

    except FileNotFoundError:
        print("Storage file not found")


def rem_task() -> None:

    task_id = input("Enter id of task to delete: ")
    
    try:
        with open("storage/store.json", 'r') as jf:
            task_list: list[Task] = json.load(jf)
            task_idx = search_task_idx(int(task_id))
            task_list.pop(task_idx)

        with open("storage/store.json", 'w') as jf:
            json.dump(task_list, jf)

    except FileNotFoundError:
        print("Storage file not found")
        