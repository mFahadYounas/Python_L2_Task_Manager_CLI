from cli.menu import Menu
from cli.store import create_store
from cli.manager import add_task, rem_task, toggle_task_status, view_all_tasks
import os

def main():
    
    if(not os.path.exists("storage/store.json")):
        create_store()

    menu = Menu()
    menu.display_menu()
    selection = menu.get_menu_input()
    
    if(selection == 1):
        add_task()
    elif(selection == 4 or selection == 5):
        toggle_task_status()
    elif(selection == 2):
        view_all_tasks()
    elif(selection == 6):
        rem_task()


if __name__ == "__main__":
    main()
