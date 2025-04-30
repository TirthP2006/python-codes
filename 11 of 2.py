# Check if the points are collinear
x1, y1 = map(int, input("Enter the coordinates of the first point (x1 y1): ").split())
x2, y2 = map(int, input("Enter the coordinates of the second point (x2 y2): ").split())
x3, y3 = map(int, input("Enter the coordinates of the third point (x3 y3): ").split())


if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
    print("The points lie on a straight line.")
else:
    print("The points do not lie on a straight line.")
