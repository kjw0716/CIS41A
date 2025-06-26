#CIS41A C2E2 Jackie Wang Team: Python Enjoyers write a circle
from ezgraphics import GraphicsWindow
import math

# Prompt user for inputs
user_name = input("Enter your name: ")
gw_width = int(input("Enter window width: "))
gw_height = int(input("Enter window height: "))
radius = float(input("Enter circle radius: "))

outline_color_input = input("Enter outline color: ")
fill_color_input = input("Enter fill color: ")

# input color colors
def parse_color(color_str):
    if "," in color_str:
        r, g, b = map(int, color_str.split(','))
        return (r, g, b)
    return color_str

outline_color = parse_color(outline_color_input)
fill_color = parse_color(fill_color_input)

# Create window and canvas
gw = GraphicsWindow(gw_width, gw_height)
gw.setTitle("CIS40 - Ch2 Ex3")
canvas = gw.canvas()

# Configure appearance
canvas.setBackground(255, 255, 224)
canvas.setTextAnchor("nw")
canvas.setLineWidth(5)
canvas.setOutline(outline_color)
canvas.setFill(fill_color)

# Draw circle
diameter = 2 * radius
upper_left_x = (gw_width / 2) - radius
upper_left_y = (gw_height / 2) - radius
canvas.drawOval(upper_left_x, upper_left_y, diameter, diameter)

# Calculate circumference and area
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Display results
text_x = 0.01 * gw_width
text_y = 0.01 * gw_height
message = (
    f"{user_name}\n"
    f"The circumference: {circumference:.2f}\n"
    f"The area: {area:.2f}"
)
canvas.drawText(text_x, text_y, message)

gw.wait()
'''
Enter your name: jackie
Enter window width: 1000
Enter window height: 1000
Enter circle radius: 200
Enter outline color: red
Enter fill color: blue

Enter your name: Jackie
Enter window width: 1500
Enter window height: 800
Enter circle radius: 300
Enter outline color: blue
Enter fill color: red
'''

