#convert video to mp3
import os
import re
import subprocess

files = os.listdir("videos")

for file in files:
    print(file)
    video_number = ""
    if "_ Camera " in file:
        video_split = file.split("_ Camera ")[1]
        video_number = re.search('\d+', video_split).group()
    else :
        video_number = file.split("_ Camera ")[0]
    video_name = "Camera"
    print( video_name + video_number)

    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{video_name}_{video_number}.mp3"])



