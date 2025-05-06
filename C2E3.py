from ezgraphics import GraphicsWindow
import math

width = int(input("Enter window width: "))
height = int(input("Enter window height: "))
radius = float(input("Enter circle radius: "))
outline_color = input("Enter outline color (e.g. red or 255,0,0): ")
fill_color = input("Enter fill color (e.g. blue or 0,255,0): ")

circle = 2 * math.pi * radius
area = math.pi * radius**2

win = GraphicsWindow(width, height)
win.setTitle("CIS40 - Ch2 Ex3")
canvas = win.canvas()
canvas.setBackground(255, 255, 224)
canvas.setTextAnchor("nw")
canvas.setLineWidth(5)

cx, cy = width / 2, height / 2
# Set colors
canvas.setOutline(outline_color)
canvas.setFill(fill_color)
# Draw circle
canvas.drawOval(cx - radius, cy - radius, 2 * radius, 2 * radius)

# Display the circumference and area
canvas.drawText(10, 10, f"Circumference: {circle:.2f}")
canvas.drawText(10, 30, f"Area: {area:.2f}")

win.wait()
