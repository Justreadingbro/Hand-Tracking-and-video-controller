import cv2
import mediapipe as mp
import pyautogui
import time
from typing import Any

mp_hands = mp.solutions.hands
hands_detector = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

prev_x_pos = None
swipe_cooldown_sec = 1.0
last_swipe_timestamp = 0
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
        total_fingers_up = sum(finger_states)
        if total_fingers_up == 5 and (current_time - last_action_timestamp) > action_cooldown_sec:
            pyautogui.press('playpause')
            last_action_timestamp = current_time
        elif total_fingers_up == 0 and (current_time - last_action_timestamp) > action_cooldown_sec:
            pyautogui.press('playpause')
            last_action_timestamp = current_time
        elif finger_states == [0, 1, 1, 0, 0] and (current_time - last_action_timestamp) > action_cooldown_sec:
            pyautogui.press('volumeup')
            last_action_timestamp = current_time
        elif finger_states == [0, 1, 1, 1, 1] and (current_time - last_action_timestamp) > action_cooldown_sec:
            pyautogui.press('volumedown')
            last_action_timestamp = current_time
        elif finger_states == [0, 1, 1, 0, 0]:
            x_pos = hand_landmarks.landmark[12].x

            if prev_x_pos is not None:
                diff = x_pos - prev_x_pos
                if abs(diff) > 0.1 and (current_time - last_swipe_timestamp) > swipe_cooldown_sec:
                    if diff > 0:
                        pyautogui.hotkey('win', 'd')
                    else:
                        pyautogui.hotkey('alt', 'tab')
                    last_swipe_timestamp = current_time

            prev_x_pos = x_pos
        else:
            prev_x_pos = None

        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    else:
        prev_x_pos = None

    cv2.imshow("Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
