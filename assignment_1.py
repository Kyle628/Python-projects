#Kyle O'Connor kyjoconn@ucsc.edu assignment 1
import math
#prompt user for the three values necessary to calculate perimeter, area, etc
sideOne = float(raw_input('What is the length of side one of the triangle?'))
sideTwo = float(raw_input('What is the length of side two of the triangle?'))
sideThree = float(raw_input('What is the length of side three of the triangle?'))
#make function to calculate perimeter
def calc_tri_perimeter(sideOne, sideTwo, sideThree):
    perimeter = sideOne + sideTwo + sideThree
    return perimeter
#make function to calculate area of a triangle using Heron's formula
def calc_tri_area(sideOne, sideTwo, sideThree):
    perimeter = calc_tri_perimeter(sideOne, sideTwo, sideThree)
    semiPerimeter = .5 * perimeter
    area = (semiPerimeter * (semiPerimeter - sideOne) * (semiPerimeter - sideTwo) * (semiPerimeter - sideThree)) ** .5
    return area
#make function to calculate each angle using area=absin(c) and radians-->degrees conversion 180/pi ~ 57.29577
def find_angle(sideOne, sideTwo, sideThree):
    area = calc_tri_area(sideOne, sideTwo, sideThree)
    angleOne = math.asin((2 * area) / (sideTwo * sideThree)) * 57.29577
    angleTwo = math.asin((2 * area) / (sideOne * sideThree)) * 57.29577
    angleThree = math.asin((2 * area) / (sideTwo * sideOne)) * 57.29577
    return angleOne, angleTwo, angleThree
perimeter = calc_tri_perimeter(sideOne, sideTwo, sideThree)
area = calc_tri_area(sideOne, sideTwo, sideThree)
three_angles = find_angle(sideOne, sideTwo, sideThree)
print 'The perimeter of your triangle is', str(perimeter)
print 'The area of your triangle is', str(area)
print 'The values of angle one , two and three are', str(three_angles)