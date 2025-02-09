import os

def get_default_audio_file_path():
    default_dir = os.path.expanduser("~/Documents")
    return os.path.join(default_dir, "recording.wav")