__author__ = 'Joe Delia'
from graphics import *


class Fractal:

    def __init__(self):
        pass

    def get_iterations(self):
        return self.iterations

    def draw_lines(self, pt1, pt2):
        line = Line(pt1, pt2)

        try:
            line.draw(self.w)
            return 1
        except GraphicsError:
            return 0


class FourFractal(Fractal):

    def __init__(self, scale, iterations, init_point, init_length, window):
        self.point = init_point
        self.length = init_length
        self.iterations = iterations
        self.scale_ratio = scale
        self.point_list = [self.point]
        self.tot_list = []
        self.w = window
        Fractal.__init__(self)

    def point_creator(self, iteration):
        ret = []
        for point in self.point_list:
            xVal = float(point.getX())
            yVal = float(point.getY())
            newXNeg = xVal - self.length * (self.scale_ratio ** iteration)
            newXPos = xVal + self.length * (self.scale_ratio ** iteration)
            newYNeg = yVal - self.length * (self.scale_ratio ** iteration)
            newYPos = yVal + self.length * (self.scale_ratio ** iteration)

            # Program will by default create an iteration at every center node
            # as well as at the end of each branch for every non .5 scaling ratio.
            # If you want to remove the central node iteration, remove
            # "Point(xVal,yVal), " from pointList under else.
            if self.scale_ratio == .5:
                points_array = [Point(newXNeg, yVal), Point(newXPos, yVal),
                    Point(xVal, newYNeg), Point(xVal, newYPos)]
            else:
                points_array = [Point(xVal, yVal), Point(newXNeg, yVal), Point(newXPos, yVal),
                    Point(xVal, newYNeg), Point(xVal, newYPos)]

            for new_point in points_array:
                if not self.draw_lines(point, new_point):
                    return -1

            ret = ret + points_array

        self.point_list = ret
        self.iterations = self.iterations + 1


class SixFractal(Fractal):

    def __init__(self, scale, iterations, init_point, init_length, window):
        self.point = init_point
        self.length = init_length
        self.iterations = iterations
        self.scale_ratio = scale
        self.point_list = [self.point]
        self.tot_list = []
        self.w = window
        Fractal.__init__(self)

    def point_creator(self, iteration):
        ret = []
        for point in self.point_list:
            xVal = float(point.getX())
            yVal = float(point.getY())

            newX1 = xVal - self.length * (self.scale_ratio ** iteration)
            newX2 = xVal + self.length * (self.scale_ratio ** iteration)
            newX3 = xVal - (self.length / 2) * (self.scale_ratio ** iteration)
            newX4 = xVal + (self.length / 2) * (self.scale_ratio ** iteration)
            newY1 = yVal - (self.length * (9. / 10)) * (self.scale_ratio ** iteration)
            newY2 = yVal + (self.length * (9. / 10)) * (self.scale_ratio ** iteration)

            # Program will by default create an iteration at every center node
            # as well as at the end of each branch for every non .5 scaling ratio.
            # If you want to remove the central node iteration, remove
            # "Point(xVal,yVal), " from pointList under else.
            if self.scale_ratio == .5:
                points_array = [Point(newX1, yVal), Point(newX2, yVal),
                    Point(newX3, newY1), Point(newX3, newY2),
                    Point(newX4, newY1), Point(newX4, newY2)]
            else:
                points_array = [Point(xVal, yVal), Point(newX1, yVal), Point(newX2, yVal),
                    Point(newX3, newY1), Point(newX3, newY2),
                    Point(newX4, newY1), Point(newX4, newY2)]

            for new_point in points_array:
                if not self.draw_lines(point, new_point):
                    return -1

            ret = ret + points_array

        self.point_list = ret
        self.iterations = self.iterations + 1
