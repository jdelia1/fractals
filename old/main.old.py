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

    # print ratio

    length = MIDPOINT / ratio

    myWin = GraphWin("Fractal Tree", WINDOW_SIZE, WINDOW_SIZE)

    for i in range(1, its + 1):
        ptList = pointCreator(ptList, i, scale, length, myWin)
        if ptList == -1:
            break

    if ptList != -1:
        myWin.getMouse()
        myWin.close()


def pointCreator(ptList, its, scale, length, win):
    pointList = []
    totList = []
    scalRat = scale
    for point in ptList:
        xVal = float(point.getX())
        yVal = float(point.getY())
        newXNeg = xVal - length * (scalRat ** (its - 1))
        newXPos = xVal + length * (scalRat ** (its - 1))
        newYNeg = yVal - length * (scalRat ** (its - 1))
        newYPos = yVal + length * (scalRat ** (its - 1))

        # Program will by default create an iteration at every center node
        # as well as at the end of each branch for every non .5 scaling ratio.
        # If you want to remove the central node iteration, remove
        # "Point(xVal,yVal), " from pointList under else.
        if scalRat == .5:
            pointList = [Point(newXNeg, yVal), Point(newXPos, yVal),
                         Point(xVal, newYNeg), Point(xVal, newYPos)]
        else:
            pointList = [Point(xVal, yVal), Point(newXNeg, yVal), Point(newXPos, yVal),
                         Point(xVal, newYNeg), Point(xVal, newYPos)]
            # Point(xVal,yVal),

        for newPt in pointList:
            if not drawLines(point, newPt, win):
                return -1

        totList = totList + pointList

    return totList


def drawLines(pt1, pt2, win):
    line = Line(pt1, pt2)
    try:
        line.draw(win)
        return 1
    except:
        print("Window Closed")
        return 0


main()
