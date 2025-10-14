from cli.menu import Menu
from cli.store import create_store
from cli.manager import actions, task_id
import time
import os
import sys


def main():
    try:
        print("Running — press Ctrl+C to exit")
        while True:
            if not os.path.exists("storage/store.json"):
                create_store()

            menu = Menu()
            menu.display_menu()
            selection = menu.get_menu_input()

            action = actions[selection]
            action()

            time.sleep(0.1)

    except KeyboardInterrupt:
        try:
            with open("memory/mem.txt", "w") as f:
                f.write(next(task_id))
        except FileNotFoundError:
            print("\nMemory directory or mem.txt not found!")

        print("\nReceived Ctrl+C — shutting down gracefully")
        sys.exit(0)


if __name__ == "__main__":
    main()
