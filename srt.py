import os
import random
import shutil
from pydub import AudioSegment
from datetime import datetime, timedelta

# 1. audio files 폴더에서 오디오 파일 목록 가져오기
audio_files_folder = "audio files"
audio_files = os.listdir(audio_files_folder)

# 2. 랜덤으로 30곡 선택하여 [오늘 날짜] 폴더로 복사
today_folder = datetime.now().strftime("%Y-%m-%d")
if not os.path.exists(today_folder):
    os.mkdir(today_folder)

selected_audio_files = random.sample(audio_files, 30)
for audio_file in selected_audio_files:
    source_path = os.path.join(audio_files_folder, audio_file)
    destination_path = os.path.join(today_folder, audio_file)
    shutil.copy2(source_path, destination_path)

# 3. [오늘 날짜] 폴더 안의 파일 순서를 랜덤으로 섞기
random.shuffle(selected_audio_files)

# 4. 자막 파일 생성 및 저장
for i, audio_file in enumerate(selected_audio_files):
    # Title 자막 생성
    title = audio_file.split(" - ")[0]

    # Artist 자막 생성
    artist = audio_file.split(" - ")[1].split(".")[0]

    # 오디오 파일의 길이(재생 시간) 가져오기
    audio_file_path = os.path.join(today_folder, audio_file)
    audio = AudioSegment.from_file(audio_file_path)
    audio_duration_seconds = len(audio) / 1000  # 밀리초(ms)를 초(s)로 변환

    # Length 자막 생성
    length_minutes = int(audio_duration_seconds // 60)
    length_seconds = int(audio_duration_seconds % 60)
    length = f"{length_minutes}:{length_seconds:02}"

    # 자막 파일 저장
    title_srt = f"{title}.srt"
    artist_srt = f"{artist}.srt"
    length_srt = f"{length}.srt"

    with open(title_srt, "w") as title_srt_file:
        title_srt_file.write(f"{i + 1}\n0:00:00,000 --> {length}\n{title}\n\n")

    with open(artist_srt, "w") as artist_srt_file:
        artist_srt_file.write(f"{i + 1}\n0:00:00,000 --> {length}\n{artist}\n\n")

    with open(length_srt, "w") as length_srt_file:
        length_srt_file.write(f"{i + 1}\n0:00:00,000 --> {length}\n{length}\n\n")

# 5. description.txt 파일 생성
description_txt = "description.txt"
with open(description_txt, "w") as desc_file:
    total_duration = 0
    for i, audio_file in enumerate(selected_audio_files):
        # 오디오 파일의 길이(재생 시간) 가져오기
        audio_file_path = os.path.join(today_folder, audio_file)
        audio = AudioSegment.from_file(audio_file_path)
        audio_duration_seconds = len(audio) / 1000  # 밀리초(ms)를 초(s)로 변환
        duration_minutes = int(audio_duration_seconds // 60)
        duration_seconds = int(audio_duration_seconds % 60)
        duration = f"{duration_minutes}:{duration_seconds:02}"

        # Title와 Artist 가져오기
        title = audio_file.split(" - ")[0]
        artist = audio_file.split(" - ")[1].split(".")[0]

        # description.txt에 기록
        desc_file.write(f"{total_duration:02}:{duration_minutes}:{duration_seconds:02} | {title} - {artist}\n")

        # 다음 곡의 시작 시간 계산
        total_duration += audio_duration_seconds

print("작업이 완료되었습니다.")
