import matplotlib.pyplot as plt
import numpy as np

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

def place_rectangles(rectangles, x, y, width, height):
    # Base case: If no rectangles left, return the current placement
    if not rectangles:
        return [(x, y, width, height)]

    # Try placing the first rectangle horizontally
    horizontal_placement = place_rectangles(rectangles[1:], x + rectangles[0].width + 1, y, width - rectangles[0].width - 1, height)
    
    # Try placing the first rectangle vertically
    vertical_placement = place_rectangles(rectangles[1:], x, y + rectangles[0].height + 1, width, height - rectangles[0].height - 1)
    
    # Choose the placement with the smaller total area
    if area(horizontal_placement) < area(vertical_placement):
        return [(x, y, rectangles[0].width, height)] + horizontal_placement
    else:
        return [(x, y, width, rectangles[0].height)] + vertical_placement

def area(rectangles):
    return sum(rect[2] * rect[3] for rect in rectangles)

# Example: Random rectangle dimensions (you can replace with actual dimensions)
rectangles = [Rectangle(20, 10), Rectangle(15, 25), Rectangle(30, 15), Rectangle(10, 20), Rectangle(25, 30)]

# Initial placement in a 100x100 unit space
placement = place_rectangles(rectangles, 0, 0, 100, 100)

# Visualization
plt.figure(figsize=(6, 6))
for rect in placement:
    plt.gca().add_patch(plt.Rectangle((rect[0], rect[1]), rect[2], rect[3], fill=None, edgecolor='b'))
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Optimal Rectangle Placement")
plt.xlabel("Width")
plt.ylabel("Height")
plt.grid(True)
plt.show()
