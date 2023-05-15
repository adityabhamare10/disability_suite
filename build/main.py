import cv2
import mediapipe as mp
import pyautogui
import time

# Set the scale factor for the mouse movement
SCALE_FACTOR = 0.8

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(
    max_num_faces=2,
    static_image_mode=False,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    refine_landmarks=True
)
screen_w, screen_h = pyautogui.size()

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w * landmark.x / SCALE_FACTOR
                screen_y = screen_h * landmark.y / SCALE_FACTOR
                pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.004:
            pyautogui.click()  # Simulate a left-click
            time.sleep(0.1)  # Add a small delay here
    cv2.imshow('Press Esc to stop', frame)
    key = cv2.waitKey(1) & 0xff
    if key == 27:  # Press Esc to stop
        break

# Release the camera and close all windows
cam.release()
cv2.destroyAllWindows()