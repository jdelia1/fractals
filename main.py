# Author: Joe Delia
# In 2012-2013, I worked on a research project involving space-filling fractals.
# I wrote a program in Python 2.7 that would draw out square- and hexagonal-shaped
# fractals.
#
# This project is porting that original project to Python 3.x, and adding additional
# functionality and speed to it as well.
# Last Edit: 7/31/2018

__author__ = 'Joe'
from graphics import *
from fractal import *

WINDOW_SIZE = 800  # Size of the window
MIDPOINT = WINDOW_SIZE / 2  # Midpoint of the window


def main():
    pt1 = Point(MIDPOINT, MIDPOINT)
    print("What kind of fractal do you want to draw?")
    f_type = get_type()
    scale = get_scale()
    its = get_iterations()

    ratio = 0
    for i in range(its):
        ratio = ratio + scale ** i

    length = MIDPOINT / ratio
    myWin = GraphWin("Fractal Tree", WINDOW_SIZE, WINDOW_SIZE)

    if f_type == 4:
        fractal = FourFractal(scale, its, pt1, length, myWin)
    else:
        fractal = SixFractal(scale, its, pt1, length, myWin)

    for iteration in range(0, fractal.get_iterations()):
        fractal.point_creator(iteration)

    try:
        myWin.getMouse()
        myWin.close()
    except GraphicsError:
        print("Window closed before execution completed")
        return 0


def get_type():
    f_type = ""

    while f_type != 4 and f_type != 6:
        f_type = input("Enter '4' for square, or '6' for hexagon: ")
        try:
            f_type = float(f_type)
        except ValueError:
            f_type = ""

    return f_type


def get_scale():
    scale = -1
    while scale <= 0.0 or scale >= 1.0:
        scale = input("Enter a scaling ratio (must be between 0 and 1): ")
        try:
            scale = float(scale)
        except ValueError:
            scale = -1

    return scale


def get_iterations():
    iterations = -1
    while iterations < 0:
        iterations = input("Enter a number of iterations (higher numbers result in slower results!): ")
        try:
            iterations = int(iterations)
        except ValueError:
            iterations = -1

    return iterations


main()
