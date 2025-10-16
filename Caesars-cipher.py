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
