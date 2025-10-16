"""
volume = width * height * depth
"""

def calculute_box_volume(width, height, depth):
    volume = width * height * depth
    return volume

def main():
    box1_volume = calculute_box_volume(10, 20, 30)
    print('Volume of box 1 is: ' + str(box1_volume))

    box2_volume = calculute_box_volume(5, 6, 7)
    print('Volume of box 2 is: ' + str(box2_volume))

