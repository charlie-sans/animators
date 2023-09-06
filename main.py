import os
import sys
import time
import importlib.util

def clear_terminal():
    sys.stdout.write("\033[2J")
    sys.stdout.flush()

def move_cursor(x, y):
    sys.stdout.write("\033[{};{}H".format(y, x))
    sys.stdout.flush()

def load_frames_from_file(file_path):
    try:
        spec = importlib.util.spec_from_file_location("frames_module", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "frames") and isinstance(module.frames, list):
            return module.frames
    except (FileNotFoundError, AttributeError):
        pass
    return None

def choose_frames_file():
    python_files = [file for file in os.listdir() if file.endswith(".py")]
    print("Choose a Python file containing the frames variable:")
    for idx, file_name in enumerate(python_files, 1):
        print(f"{idx}. {file_name}")

    while True:
        try:
            choice = int(input("Enter the number of the file: "))
            if 1 <= choice <= len(python_files):
                return python_files[choice - 1]
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def spin_animation(frames):
    for _ in range(1):
        for frame in frames:
            move_cursor(1, 1)
            sys.stdout.write(frame)
            sys.stdout.flush()
            os.system("cls")
            time.sleep(0.001)

if __name__ == "__main__":
    try:
        clear_terminal()
        frames_file = choose_frames_file()
        frames = load_frames_from_file(frames_file)
        if frames is not None:
            spin_animation(frames)
        else:
            print("Error: Invalid file or frames not found.")
        clear_terminal()
    except KeyboardInterrupt:
        # If the user presses Ctrl+C, clear the terminal before exiting
        clear_terminal()
