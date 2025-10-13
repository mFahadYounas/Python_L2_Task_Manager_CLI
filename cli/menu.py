class Menu:
    
    def __init__(self):
        self.menu_options = (
            "Add a new task",
            "View all tasks",
            "View completed tasks",
            "Mark a task as completed",
            "Mark a task as pending",
            "Delete a task"
        )
        self.menu_input = 0

    def __validate_menu_input(self):
        menu_input_int = 0
        try:
            menu_input_int = int(self.menu_input)
        except ValueError:
            return False

        if(menu_input_int < 1 or menu_input_int > len(self.menu_options)):
            return False
        
        return True

    def display_menu(self):
        print("Select one of the options given below:")

        for i in range(len(self.menu_options)):
            print(f"{i + 1}. {self.menu_options[i]}")


    def get_menu_input(self):
        self.menu_input = input("Your input: ")

        if(not self.__validate_menu_input()):
            raise ValueError("Invalid input: Input can only be integer within menu option range!")

        return int(self.menu_input)