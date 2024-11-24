
init -100 python:

    import logging

    logging.basicConfig(
        level=logging.DEBUG,  # Set the logging level
        format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log format
        filename=f"{renpy.config.gamedir}/my_log.txt",  # Log output file
        filemode='w'  # Overwrite the log file each time
    )

    import os

    is_night = True

    def create_animations_from_directory(directory, duration=0.25):
        """
        Scans a directory and creates two-frame animations for images with matching patterns.
        :param directory: Path to the directory containing animation frames.
        :param duration: Duration of each frame in the animation.
        """
        # Get all files in the directory
        files = sorted(os.listdir(f"{renpy.config.gamedir}/{directory}"))

        # Dictionary to group frames by their base name
        animations = {}

        for file in files:
            # Assume the format is 'prefix_frameN.png' (e.g., 'image1_frame1.png')
            if "_" in file and file.endswith(".png"):
                base_name, frame = file.rsplit("_", 1)
                frame = frame.split(".")[0]  # Remove the extension
                if base_name not in animations:
                    animations[base_name] = []
                animations[base_name].append(file)

        # Create animations for groups with exactly 2 frames
        for name, frames in animations.items():
            if len(frames) == 2:
                # Sort frames to ensure correct order
                frames.sort()
                create_two_frame_animation(f"{name}_gif", f"{directory}/{frames[0]}", f"{directory}/{frames[1]}", duration)

    def create_two_frame_animation(name, frame1, frame2, duration):
        """
        Creates a two-frame animation.
        :param name: Name of the animation.
        :param frame1: Path to the first frame.
        :param frame2: Path to the second frame.
        :param duration: Duration of each frame.
        """
        logging.info(f"Creating animation: {name} with frames {frame1}, {frame2}")
        animation = Animation(frame1, duration, frame2, duration, repeat=True)
        renpy.exports.image(name, animation)
    
    create_animations_from_directory("two-frame-animation")
