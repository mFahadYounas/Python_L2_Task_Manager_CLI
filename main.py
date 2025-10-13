from cli.menu import Menu

def main():
    menu = Menu()

    menu.display_menu()
    menu.get_menu_input()

if __name__ == "__main__":
    main()
