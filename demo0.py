from ezgraphics import GraphicsWindow

win = GraphicsWindow()
canvas = win.canvas()
canvas.drawText(100, 100, "Hello, EzGraphics!")
win.redraw()
win.wait()
