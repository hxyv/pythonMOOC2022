import math
student = 11
size = 3
if student % size == 0:
    print("Number of groups formed:", student // size)
elif student % size != 0:
    print("Number of groups formed:", math.floor(student // size) + 1)
