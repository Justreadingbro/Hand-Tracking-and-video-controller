import cv2
import mediapipe as mp
import pyautogui
import time
from typing import Any

mp_hands = mp.solutions.hands
hands_detector = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

action_cooldown_sec = 0.5
last_action_timestamp = 0

def get_finger_states(landmarks):
    thumb_up = 1 if landmarks[4].x < landmarks[3].x else 0
    fingers_up = [
        thumb_up,
        1 if landmarks[8].y < landmarks[6].y else 0,
        1 if landmarks[12].y < landmarks[10].y else 0,
        1 if landmarks[16].y < landmarks[14].y else 0,
        1 if landmarks[20].y < landmarks[18].y else 0
    ]
    return fingers_up

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results: Any = hands_detector.process(rgb_frame)

    current_time = time.time()

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        finger_states = get_finger_states(hand_landmarks.landmark)

        finger_code = ''.join(map(str, finger_states))

        if finger_code == '00000' and (current_time - last_action_timestamp) > action_cooldown_sec:
            pyautogui.press('playpause') 
            print("Gesture: 00000 → Pause")
            last_action_timestamp = current_time

        elif finger_code == '11111' and (current_time - last_action_timestamp) > action_cooldown_sec:
            pyautogui.press('playpause') 
            print("Gesture: 11111 → Play")
            last_action_timestamp = current_time

        elif finger_code == '01100' and (current_time - last_action_timestamp) > action_cooldown_sec:
            pyautogui.press('volumeup')
            print("Gesture: 01100 → Volume Up")
            last_action_timestamp = current_time

        elif finger_code == '01111' and (current_time - last_action_timestamp) > action_cooldown_sec:
            pyautogui.press('volumedown')
            print("Gesture: 01111 → Volume Down")
            last_action_timestamp = current_time

        elif finger_code == '11000' and (current_time - last_action_timestamp) > action_cooldown_sec:
            pyautogui.hotkey('win', 'd')
            print("Gesture: 11000 → Show Desktop")
            last_action_timestamp = current_time

        elif finger_code == '11100' and (current_time - last_action_timestamp) > action_cooldown_sec:
            pyautogui.hotkey('alt', 'tab')
            print("Gesture: 11100 → Switch App")
            last_action_timestamp = current_time

        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
