from typing import TypedDict


class Task(TypedDict):
    id: str
    title: str
    description: str
    status: bool