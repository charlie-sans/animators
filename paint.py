def read_ascii_art_file(file_path):
    frames = {}
    current_frame = None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            if line.startswith('==='):
                # Start a new frame
                current_frame = []
                frames[line[3:]] = current_frame
            elif current_frame is not None:
                current_frame.append(line)

    return frames


def print_frame(frame):
    for line in frame:
        print(line)


def main():
    file_path = "ascii.txt"
    frames = read_ascii_art_file(file_path)

    # Print and see each frame
    for frame_name, frame in frames.items():
        print(f"Frame: {frame_name}")
        print_frame(frame)
        print("\n")

    # You can access a specific frame like this:
    # print_frame(frames['frame1'])


if __name__ == "__main__":
    main()
