import os

# Paths
source_folder = "selected musics"
playlist_path = os.path.join("mixed list", "mixed_music_list.txt")

# Read mixed_music_list.txt
with open(playlist_path, "r") as f:
    music_list = [line.strip() for line in f.readlines()]

# Rename files in selected musics folder based on order in mixed_music_list.txt
for index, music in enumerate(music_list, 1):
    old_path = os.path.join(source_folder, music)
    new_name = f"{index:02d}_{music}"
    new_path = os.path.join(source_folder, new_name)
    os.rename(old_path, new_path)

print(f"Files in {source_folder} have been renamed based on the order in {playlist_path}.")
