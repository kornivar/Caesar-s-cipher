def get_folder_path():
    path = input("Enter the path to the folder:")
    return path

def choose_action():
    while True:
        action = input("Select action (1 - encrypt, 2 - decrypt):")
        if action in ("1", "2"):
            return action
        else:
            print("Enter 1 or 2.")

def choose_file():
    file = input("Enter the name of the text file (.txt):")
    return file

print("=== Program for working with the Caesar cipher ===")
folder = get_folder_path()
file_name = choose_file()
action = choose_action()
