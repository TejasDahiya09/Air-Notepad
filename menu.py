import cv2
import numpy as np
from tools import current_tool, current_color, current_color_name, color_palette, Tool
from config import canvas_height, menu_width

def draw_menu(frame):
    menu_bg = np.ones((canvas_height, menu_width, 3), dtype=np.uint8) * 40
    y_offset = 20

    cv2.putText(menu_bg, "TOOLS", (10, y_offset),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
    y_offset += 30

    tools = [
        (Tool.PEN, "Pen"),
        (Tool.BRUSH, "Brush"),
        (Tool.ERASER, "Eraser")
    ]
    tool_buttons = []
    for tool_id, tool_name in tools:
        color = (100, 200, 100) if current_tool == tool_id else (80, 80, 80)
        cv2.rectangle(menu_bg, (10, y_offset), (110, y_offset + 30), color, -1)
        cv2.putText(menu_bg, tool_name, (20, y_offset + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255), 1)
        tool_buttons.append((10, y_offset, 110, y_offset + 30, tool_id))
        y_offset += 40

    y_offset += 20
    cv2.putText(menu_bg, "COLORS", (10, y_offset),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
    y_offset += 30

    color_buttons = []
    for i, (name, color) in enumerate(color_palette):
        row = i // 2
        col = i % 2
        x = 10 + col * 55
        y = y_offset + row * 45

        if name == current_color_name:
            cv2.rectangle(menu_bg, (x - 3, y - 3), (x + 43, y + 43), (255,255,0), 2)

        cv2.rectangle(menu_bg, (x, y), (x + 40, y + 40), color, -1)
        color_buttons.append((x, y, x + 40, y + 40, name, color))

    clear_y = canvas_height - 50
    cv2.rectangle(menu_bg, (10, clear_y), (110, clear_y + 35), (0, 0, 150), -1)
    cv2.putText(menu_bg, "CLEAR", (25, clear_y + 23),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
    clear_button = (10, clear_y, 110, clear_y + 35, "clear")

    frame[0:canvas_height, 0:menu_width] = menu_bg

    return tool_buttons, color_buttons, clear_button


def check_menu_interaction(x, y, tool_buttons, color_buttons, clear_button, canvas):
    from tools import current_tool, current_color, current_color_name

    for x1, y1, x2, y2, tool_id in tool_buttons:
        if x1 <= x <= x2 and y1 <= y <= y2:
            globals()["current_tool"] = tool_id
            return True

    for x1, y1, x2, y2, name, color in color_buttons:
        if x1 <= x <= x2 and y1 <= y <= y2:
            globals()["current_color"] = color
            globals()["current_color_name"] = name
            return True

    x1, y1, x2, y2, _ = clear_button
    if x1 <= x <= x2 and y1 <= y <= y2:
        canvas[:] = 0
        return True

    return False
