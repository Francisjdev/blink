import cv2
import mediapipe as mp
import numpy as np
from datetime import datetime


def eye_aspect_ratio(coordinates):
    d_A = np.linalg.norm(np.array(coordinates[1]) - np.array(coordinates[5]))
    d_B = np.linalg.norm(np.array(coordinates[2]) - np.array(coordinates[4]))
    d_C = np.linalg.norm(np.array(coordinates[0]) - np.array(coordinates[3]))

    return (d_A + d_B) / (2 * d_C)


cap = cv2.VideoCapture(0)


mp_face_mesh = mp.solutions.face_mesh
index_left_eye = [33, 160, 158, 133, 153, 144]
index_right_eye = [362, 385, 387, 263, 373, 380]
EAR_THRESH = 0.17
NUM_FRAMES = 2
aux_counter = 0
blink_counter = 0
t1 = 0
t2 = 0
t3 = 0


with mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1) as face_mesh:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        height, width, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(frame_rgb)

        coordinates_left_eye = []
        coordinates_right_eye = []

        if results.multi_face_landmarks is not None:
            for face_landmarks in results.multi_face_landmarks:
                for index in index_left_eye:
                    x = int(face_landmarks.landmark[index].x * width)
                    y = int(face_landmarks.landmark[index].y * height)
                    coordinates_left_eye.append([x, y])

                    cv2.circle(frame, (x, y), 2, (0, 255, 255), 1)
                    cv2.circle(frame, (x, y), 1, (128, 0, 255), 1)
                for index in index_right_eye:
                    x = int(face_landmarks.landmark[index].x * width)
                    y = int(face_landmarks.landmark[index].y * height)
                    coordinates_right_eye.append([x, y])
                    cv2.circle(frame, (x, y), 2, (128, 0, 255), 1)
                    cv2.circle(frame, (x, y), 1, (0, 255, 255), 1)

                ear_left_eye = eye_aspect_ratio(coordinates_left_eye)
                ear_right_eye = eye_aspect_ratio(coordinates_right_eye)
                ear = (ear_left_eye + ear_right_eye) / 2
                # print("ear_left_eye:", ear_left_eye, " ear_right_eye:", ear_right_eye)
                print(ear)

                # if ear < EAR_THRESH:
                #     aux_counter += 1

                # else:
                #     if aux_counter >= NUM_FRAMES:
                #         aux_counter = 0
                #         blink_counter += 1
                #         print(blink_counter)
                #         if blink_counter == 1:
                #             t1 = datetime.now()
                #             print("primer parpadeo")
                #         if blink_counter == 3:
                #             t2 = datetime.now()
                #             t3 = t2 - t1
                #             print("van {} microsegundos".format(t3.microseconds))
                #             if t3.microseconds < 500000 and blink_counter == 3:
                #                 print("tele ")
                #                 blink_counter = 0
                #         if blink_counter == 4:
                #             t2 = datetime.now()
                #             t3 = t2 - t1
                #             if t3.microseconds < 300000 and blink_counter == 4:
                #                 print("AYUDA ")
                #                 blink_counter = 0
                #             blink_counter = 0

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
