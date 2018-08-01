from graphics import *


def main():
    WINDOW_SIZE = 1000
    MIDPOINT = WINDOW_SIZE / 2
    pt1 = Point(MIDPOINT, MIDPOINT)
    its = int(input("How many iterations?: "))
    scale = float(input("What is the scaling ratio? (Must be a float!): "))
    ptList = [pt1]

    expVal = 0
    ratio = 0
    for i in range(its):
        ratio = ratio + scale ** i

    length = MIDPOINT / ratio

    myWin = GraphWin("Fractal Tree", WINDOW_SIZE, WINDOW_SIZE)

    for i in range(1, its + 1):
        ptList = pointCreator(ptList, i, scale, length, myWin)

    myWin.getMouse()
    myWin.close()


def pointCreator(ptList, its, scale, length, win):
    pointList = []
    totList = []
    scalRat = scale
    for point in ptList:
        xVal = float(point.getX())
        yVal = float(point.getY())

        newX1 = xVal - length * (scalRat ** (its - 1))
        newX2 = xVal + length * (scalRat ** (its - 1))
        newX3 = xVal - (length / 2) * (scalRat ** (its - 1))
        newX4 = xVal + (length / 2) * (scalRat ** (its - 1))
        newY1 = yVal - (length * (9. / 10)) * (scalRat ** (its - 1))
        newY2 = yVal + (length * (9. / 10)) * (scalRat ** (its - 1))

        # Program will by default create an iteration at every center node
        # as well as at the end of each branch for every non .5 scaling ratio.
        # If you want to remove the central node iteration, remove
        # "Point(xVal,yVal), " from pointList under else.
        if scalRat == .5:
            pointList = [Point(newX1, yVal), Point(newX2, yVal),
                         Point(newX3, newY1), Point(newX3, newY2),
                         Point(newX4, newY1), Point(newX4, newY2)]
        else:
            pointList = [Point(xVal, yVal), Point(newX1, yVal), Point(newX2, yVal),
                         Point(newX3, newY1), Point(newX3, newY2),
                         Point(newX4, newY1), Point(newX4, newY2)]

        for newPt in pointList:
            drawLines(point, newPt, win)

        totList = totList + pointList

    return totList


def drawLines(pt1, pt2, win):
    line = Line(pt1, pt2)
    line.draw(win)


main()
