import cv2
import os

def extract_frames(video_path, output_folder):
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    while success:
        frame_path = os.path.join(output_folder, f"frame_{count}.jpg")
        cv2.imwrite(frame_path, image)
        success, image = vidcap.read()
        count += 1
    vidcap.release()

videos_folder = 'videos'
output_folder = 'frames'

for video_file in os.listdir(videos_folder):
    video_path = os.path.join(videos_folder, video_file)
    extract_frames(video_path, output_folder)
