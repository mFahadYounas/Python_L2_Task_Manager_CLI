from models.tasks import Task
import json
from .utils import search_task_idx, format_task
from .decorators import log_info
from uuid import uuid4


class TaskManager:
    def __init__(self) -> None:
        self.tasks: list[Task] = []
        self.__load_tasks()

    def __load_tasks(self) -> None:
        try:
            with open("storage/store.json", "r") as jf:
                self.tasks = json.load(jf)
        except FileNotFoundError:
            print("Storage file not found")

    def __save_tasks(self) -> None:
        try:
            with open("storage/store.json", "w") as jf:
                json.dump(self.tasks, jf, indent=2)

        except FileNotFoundError:
            print("Storage file not found")

    @log_info
    def __add_task(self) -> None:
        new_task: Task = {
            "id": str(uuid4()),
            "title": "",
            "description": "",
            "status": False,
        }

        new_task["title"] = input("Enter task title: ")
        new_task["description"] = input("Enter task description (optional): ")
        self.tasks.append(new_task)
        self.__save_tasks()

    @log_info
    def __rem_task(self) -> None:
        task_id = input("Enter id of task to delete: ")
        task_idx = search_task_idx(self.tasks, task_id)
        if task_idx >= 0:
            self.tasks.pop(task_idx)
        else:
            print("Task with given ID does not exist!")
        self.__save_tasks()

    @log_info
    def __toggle_task_status(self) -> None:
        task_id = input("Enter id of task to toggle status: ")
        task_idx = search_task_idx(self.tasks, task_id)
        if task_idx >= 0:
            self.tasks[task_idx]["status"] = not self.tasks[task_idx]["status"]
        else:
            print("Task with given ID does not exist!")
        self.__save_tasks()

    @log_info
    def __view_all_tasks(self) -> None:
        print("ID\t\tTitle\t\tDescription\t\tStatus")
        for task in self.tasks:
            print(format_task(task))

    @log_info
    def __view_all_completed(self) -> None:
        print("ID\t\tTitle\t\tDescription\t\tStatus")
        for task in self.tasks:
            if task["status"]:
                print(format_task(task))

    def call_action(self, action_num: int):
        actions = {
            1: self.__add_task,
            2: self.__view_all_tasks,
            3: self.__view_all_completed,
            4: self.__toggle_task_status,
            5: self.__toggle_task_status,
            6: self.__rem_task,
        }
        actions[action_num]()
