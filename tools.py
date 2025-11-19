class Tool:
    PEN = "pen"
    BRUSH = "brush"
    ERASER = "eraser"

# Colors
color_palette = [
    ("Red", (0, 0, 255)),
    ("Blue", (255, 0, 0)),
    ("Green", (0, 255, 0)),
    ("Yellow", (0, 255, 255)),
    ("Purple", (255, 0, 255)),
    ("White", (255, 255, 255)),
    ("Orange", (0, 165, 255)),
    ("Pink", (203, 192, 255))
]

# Current state
current_tool = Tool.PEN
current_color = (255, 255, 255)
current_color_name = "White"

tool_properties = {
    Tool.PEN: {"thickness": 3, "alpha": 1.0},
    Tool.BRUSH: {"thickness": 8, "alpha": 0.7},
    Tool.ERASER: {"thickness": 20, "alpha": 1.0}
}
