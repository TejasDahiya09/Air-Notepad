import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8,
    max_num_hands=2
)

def get_hand_label(hand_landmarks, handedness):
    return handedness.classification[0].label

def detect_pinch(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

    distance = np.sqrt(
        (thumb_tip.x - index_tip.x) ** 2 +
        (thumb_tip.y - index_tip.y) ** 2
    )

    return distance < 0.05
