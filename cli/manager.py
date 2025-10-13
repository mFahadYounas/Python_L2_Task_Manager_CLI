from models.tasks import Task
import json

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
            data.append(new_task)
        
        with open("storage/store.json", 'w') as jf:
            json.dump(data, jf, indent=2)

    except FileNotFoundError:
        print("Storage file not found")