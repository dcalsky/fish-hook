import os
from .settings import FISH_HOOK_CONFIG_NAME


def find_main_directory(path):
    current_path = path
    if not os.path.exists(os.path.join(current_path, FISH_HOOK_CONFIG_NAME)):
        parent_directory = os.path.dirname(current_path)
        # If return root
        if parent_directory == current_path:
            return None
        return find_main_directory(parent_directory)
    else:
        return current_path
