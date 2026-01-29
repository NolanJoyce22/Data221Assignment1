import math
def circle_area_coverage_comparison_of_two_circles(radius_of_circle1, radius_of_circle2):
    try:
        #Convert radii to ints and handle errors that may occur
        radius_of_circle1 = int(radius_of_circle1)
        radius_of_circle2 = int(radius_of_circle2)
        if radius_of_circle1 <= 0 or radius_of_circle2 <= 0:
            return "Radii must both be positive integers"
    except ValueError:
        return "Radii must be integers"
    #Compute each area
    area1 = math.pi*(radius_of_circle1**2)
    area2 = math.pi*(radius_of_circle2**2)
    #Determine the smaller area and compute the percentage it overlaps with the larger area
    if area1 >= area2:
          percentage_smaller_circle_covers_of_larger_circle =    (area2/area1) * 100
    else:
        percentage_smaller_circle_covers_of_larger_circle = (area1 / area2) * 100


    return percentage_smaller_circle_covers_of_larger_circle

print(circle_area_coverage_comparison_of_two_circles(5,3))
