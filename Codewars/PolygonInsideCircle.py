# reverses all the words that are >= 5 chars
def area_of_polygon_inside_circle(circle_radius, number_of_sides):
    import math
    from math import sin
    area = round(.5*number_of_sides*circle_radius*circle_radius*sin(2*math.pi/number_of_sides), 3)
    print(area)
    pass

def main():
    circle_radius = 4
    number_of_sides = 5
    area_of_polygon_inside_circle(circle_radius, number_of_sides)

if __name__ == '__main__':
    main()