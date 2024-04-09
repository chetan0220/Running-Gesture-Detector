import os
import cv2

OUTPUT_VIDEOS_DIR = '/content/drive/MyDrive/Running_Gesture_Detector/data/outputVideos'

video_path = 'path to the video to be tested'
video_name = os.path.basename(video_path)
video_path_out = os.path.join(OUTPUT_VIDEOS_DIR, f'{video_name}_out.mp4')
trained_model = 'runs/detect/YOLOv8m_Adamax2/weights/best.pt'

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
H, W, _ = frame.shape
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

threshold = 0.3

while ret:
    results = trained_model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    out.write(frame)
    ret, frame = cap.read()

cap.release()
out.release()
cv2.destroyAllWindows()
