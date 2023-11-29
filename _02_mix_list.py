import os
import random

# 폴더 경로 설정
source_folder = "selected musics"
destination_folder = "mixed list"

# 만약 목적지 폴더가 존재하지 않으면 생성
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 폴더 내의 모든 mp3 파일 목록 가져오기
mp3_files = [f for f in os.listdir(source_folder) if f.endswith('.mp3')]

# mp3 파일들의 순서를 무작위로 섞기
random.shuffle(mp3_files)

# 결과를 txt 파일로 저장하기
with open(os.path.join(destination_folder, "mixed_music_list.txt"), "w") as file:
    for mp3 in mp3_files:
        file.write(mp3 + "\n")

print(f"Shuffled list saved to {destination_folder}/mixed_music_list.txt.")
