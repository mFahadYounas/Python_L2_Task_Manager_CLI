from typing import TypedDict
from typing import Literal


class Task(TypedDict):
    id: str
    title: str
    description: str
    status: Literal["pending", "complete"]