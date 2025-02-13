# utils.py

import os
import sys

def resource_path(relative_path):
    """
    Get the absolute path to a resource, handling both development and PyInstaller builds.
    
    Parameters:
        relative_path (str): The relative path to the resource (e.g., 'assets/icon.ico').
    
    Returns:
        str: The absolute path to the resource.
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # If not running as a PyInstaller bundle, use the current directory
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


def get_default_audio_file_path():
    """
    Get the default path for saving audio files.

    Returns:
        str: The default file path for saving recordings.
    """
    default_dir = os.path.expanduser("~/Documents")
    return os.path.join(default_dir, "recording.wav")