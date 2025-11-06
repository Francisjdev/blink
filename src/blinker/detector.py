import cv2
import mediapipe as mp
from src.notifier.notifier import notify_message
import numpy as np
from src.utils.time_utils import get_timestamp


def calculate_eye_aspect_ratio(eye_points):
    """Compute the eye aspect ratio (EAR) from six eye landmarks."""
    vertical_1 = np.linalg.norm(np.array(eye_points[1]) - np.array(eye_points[5]))
    vertical_2 = np.linalg.norm(np.array(eye_points[2]) - np.array(eye_points[4]))
    horizontal = np.linalg.norm(np.array(eye_points[0]) - np.array(eye_points[3]))
    return (vertical_1 + vertical_2) / (2 * horizontal)


# Initialize webcam
camera = cv2.VideoCapture(0)

# Mediapipe Face Mesh setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh_detector = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)

# Landmark indices for eyes (based on Mediapipe face mesh model)
LEFT_EYE_INDICES = [33, 160, 158, 133, 153, 144]
RIGHT_EYE_INDICES = [362, 385, 387, 263, 373, 380]
BLINK_TRESHOLD = 0.15


def blink_detection():
    eyes_open = True
    while True:
        success, frame = camera.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        frame_for_detection = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_landmarks_data = face_mesh_detector.process(frame_for_detection)

        left_eye_points = []
        right_eye_points = []

        if face_landmarks_data.multi_face_landmarks:
            for face_landmarks in face_landmarks_data.multi_face_landmarks:
                for index in LEFT_EYE_INDICES:
                    x = int(face_landmarks.landmark[index].x * frame_width)
                    y = int(face_landmarks.landmark[index].y * frame_height)
                    left_eye_points.append([x, y])
                    cv2.circle(frame, (x, y), 2, (0, 255, 255), -1)
                for index in RIGHT_EYE_INDICES:
                    x = int(face_landmarks.landmark[index].x * frame_width)
                    y = int(face_landmarks.landmark[index].y * frame_height)
                    right_eye_points.append([x, y])
                    cv2.circle(frame, (x, y), 2, (255, 0, 255), -1)

                left_ear = calculate_eye_aspect_ratio(left_eye_points)
                right_ear = calculate_eye_aspect_ratio(right_eye_points)
                average_ear = (left_ear + right_ear) / 2
                print("EAR:", round(average_ear, 3))
                if average_ear < BLINK_TRESHOLD and eyes_open:
                    eyes_open = False
                    payload = {
                        "blink_detected": True,
                        "timestamp": get_timestamp(),
                        "ear": average_ear,
                    }
                    print(payload)
                    notify_message(payload)
                elif (average_ear >= BLINK_TRESHOLD) and not eyes_open:
                    eyes_open = True
                else:
                    payload = {
                        "blink_detected": False,
                        "timestamp": None,
                        "ear": average_ear,
                    }
                    print(payload)

        cv2.imshow("Blink Detector - Debug View", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


blink_detection()
