from cli.menu import Menu
from cli.store import create_store
from cli.TaskManager import TaskManager
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

            tm = TaskManager()
            tm.call_action(selection)

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nReceived Ctrl+C — shutting down gracefully")
        sys.exit(0)


if __name__ == "__main__":
    main()
