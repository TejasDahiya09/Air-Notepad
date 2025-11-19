import cv2
from tools import current_tool, current_color, tool_properties, Tool
from config import smooth_factor, menu_width

prev_x, prev_y = None, None

def smooth_point(new, old):
    if old is None:
        return new
    return int(smooth_factor * new + (1 - smooth_factor) * old)

def draw_on_canvas(x, y, canvas):
    global prev_x, prev_y

    if x <= menu_width:
        prev_x, prev_y = None, None
        return

    x_s = smooth_point(x, prev_x)
    y_s = smooth_point(y, prev_y)

    if prev_x is not None:
        props = tool_properties[current_tool]
        thickness = props["thickness"]
        color = (0, 0, 0) if current_tool == Tool.ERASER else current_color
        cv2.line(canvas, (prev_x, prev_y), (x_s, y_s), color, thickness)

    prev_x, prev_y = x_s, y_s
