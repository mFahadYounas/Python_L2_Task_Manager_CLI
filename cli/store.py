import json

def create_store() -> None:
    with open("storage/store.json", 'w') as jf:
        json.dump([], jf)