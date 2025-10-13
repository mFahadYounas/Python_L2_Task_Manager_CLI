from typing import TypedDict
from typing import Literal


class Task(TypedDict):
    id: int
    title: str
    description: str
    status: Literal["pending", "complete"]