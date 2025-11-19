import cv2
import numpy as np
from gestures import hands, detect_pinch, get_hand_label
from menu import draw_menu, check_menu_interaction
from drawing import draw_on_canvas
from config import canvas_width, canvas_height
from tools import current_tool, current_color_name

canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, canvas_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, canvas_height)

left_hand_pinched = False

print("Air Notepad Started!")
print("Use LEFT hand to select tools/colors (pinch gesture)")
print("Use RIGHT hand to draw (index finger extended)")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    tool_buttons, color_buttons, clear_button = draw_menu(frame)

    if results.multi_hand_landmarks and results.multi_handedness:
        for lm, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):

            label = get_hand_label(lm, handedness)
            index_tip = lm.landmark[8]
            x = int(index_tip.x * canvas_width)
            y = int(index_tip.y * canvas_height)

            # LEFT HAND = menu interaction
            if label == "Left":
                is_pinching = detect_pinch(lm)

                if is_pinching and not left_hand_pinched:
                    check_menu_interaction(x, y, tool_buttons, color_buttons, clear_button, canvas)
                    left_hand_pinched = True
                elif not is_pinching:
                    left_hand_pinched = False

            # RIGHT HAND = drawing
            elif label == "Right":
                draw_on_canvas(x, y, canvas)

    output = cv2.addWeighted(frame, 0.6, canvas, 0.4, 0)

    status = f"Tool: {current_tool.upper()} | Color: {current_color_name}"
    cv2.putText(output, status, (130, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)

    cv2.imshow("Air Notepad", output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Air Notepad closed!")
