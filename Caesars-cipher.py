from pathlib import Path

def get_directory(dir_path):

    p = Path(dir_path)

    if not p.exists():
        return False
    elif not p.is_dir():
        return False
    else:
        return True