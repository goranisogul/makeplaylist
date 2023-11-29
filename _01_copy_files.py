import os
import shutil
import random
from datetime import datetime

# 폴더 경로 설정
source_folder = "audio files"
destination_folder = "selected musics"

# 만약 목적지 폴더가 존재하지 않으면 생성
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 폴더 내의 모든 mp3 파일을 가져오기
mp3_files = [f for f in os.listdir(source_folder) if f.endswith('.mp3')]

# mp3 파일들 중 무작위로 20개 선택 (만약 20개 미만의 파일이 있으면, 그 파일 전체를 선택)
selected_files = random.sample(mp3_files, min(30, len(mp3_files)))

# 선택된 파일들을 새로운 폴더로 복사
for file in selected_files:
    shutil.copy2(os.path.join(source_folder, file), destination_folder)

print(f"{len(selected_files)} files have been copied to {destination_folder}.")
