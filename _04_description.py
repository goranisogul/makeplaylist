import os
import eyed3


def get_duration(file_path):
    """Get the duration of an mp3 file"""
    audio = eyed3.load(file_path)
    return int(audio.info.time_secs)


def format_time_description(seconds):
    """Convert seconds to mm:ss format for the description"""
    m, s = divmod(seconds, 60)
    return f"{m:02d}:{s:02d}"


# Paths
source_folder = "selected musics"
playlist_path = os.path.join("mixed list", "mixed_music_list.txt")
description_folder = "description"

# Ensure the description folder exists
if not os.path.exists(description_folder):
    os.makedirs(description_folder)

description_path = os.path.join(description_folder, "description.txt")

# Read mixed_music_list.txt
with open(playlist_path, "r") as f:
    music_list = [line.strip() for line in f.readlines()]

# Calculate starting times and write to description.txt
start_time = 0

with open(description_path, "w") as desc_file:
    for music in music_list:
        duration = get_duration(os.path.join(source_folder, music))

        # Extract song title and artist
        parts = music.split('ES_')[1].split(' - ')
        title, artist = parts[0], parts[1].replace('.mp3', '')

        desc_file.write(f"{format_time_description(start_time)} {title} - {artist}\n")

        start_time += duration

print(f"Description saved to {description_path}.")
