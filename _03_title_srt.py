import os
import eyed3
from datetime import timedelta


def get_duration(file_path):
    """Get the duration of an mp3 file"""
    audio = eyed3.load(file_path)
    return int(audio.info.time_secs)


def format_time_srt(seconds):
    """Convert seconds to hh:mm:ss:00 format"""
    return str(timedelta(seconds=seconds)) + ":00"


def format_time_duration(seconds):
    """Convert seconds to mm:ss format"""
    m, s = divmod(seconds, 60)
    return f"{m:02d}:{s:02d}"


# Paths
source_folder = "selected musics"
playlist_path = os.path.join("mixed list", "mixed_music_list.txt")
srt_folder = "srt"

if not os.path.exists(srt_folder):
    os.makedirs(srt_folder)

title_srt_path = os.path.join(srt_folder, "title.srt")
artist_srt_path = os.path.join(srt_folder, "artist.srt")
running_time_srt_path = os.path.join(srt_folder, "running time.srt")

# Read mixed_music_list.txt
with open(playlist_path, "r") as f:
    music_list = [line.strip() for line in f.readlines()]

# Extract song titles, artists and calculate durations
start_time = 0
counter = 1

with open(title_srt_path, "w") as title_srt, open(artist_srt_path, "w") as artist_srt, open(running_time_srt_path,
                                                                                            "w") as time_srt:
    for music in music_list:
        duration = get_duration(os.path.join(source_folder, music))
        parts = music.split('ES_')[1].split(' - ')
        title, artist = parts[0], parts[1].replace('.mp3', '')

        # Write to title.srt
        title_srt.write(f"{counter}\n")
        title_srt.write(f"{format_time_srt(start_time)} --> {format_time_srt(start_time + duration)}\n")
        title_srt.write(f"{title}\n\n")

        # Write to artist.srt
        artist_srt.write(f"{counter}\n")
        artist_srt.write(f"{format_time_srt(start_time)} --> {format_time_srt(start_time + duration)}\n")
        artist_srt.write(f"{artist}\n\n")

        # Write to running time.srt
        time_srt.write(f"{counter}\n")
        time_srt.write(f"{format_time_srt(start_time)} --> {format_time_srt(start_time + duration)}\n")
        time_srt.write(f"{format_time_duration(duration)}\n\n")

        start_time += duration
        counter += 1

print(f"Subtitles saved to {title_srt_path}, {artist_srt_path} and {running_time_srt_path}.")
