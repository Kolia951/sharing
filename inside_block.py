import itertools


def two_lines(line1, line2):
    """
    Finds a coordinate (x,y) of intersecting of two infinite lines
        Parameters:
            line1 - line two points as ((x,y), (x,y))
            line2 - line two points as ((x,y), (x,y))
    """
    x1 = line1[0][0]
    x2 = line1[1][0]
    x3 = line2[0][0]
    x4 = line2[1][0]
    
    y1 = line1[0][1]
    y2 = line1[1][1]
    y3 = line2[0][1]
    y4 = line2[1][1]
    
    x_part1 = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))
    x_part2 = ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    try:
        px = x_part1 / x_part2
    except:
        px = 0
    
    y_part1 = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))
    y_part2 = ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    try:
        py = y_part1 / y_part2
    except:
        py = 0
    
    return (px, py)
    

def is_inside(polygon, point):

    max_x = max(polygon)[0]
    point_x = point[0]
    point_y = point[1]
    point2line = (point, (max_x+1, point_y))

    crossing = 0
    cross_points = []
    
    all_lines = [pair for pair in itertools.pairwise(polygon)]
    all_lines.append((polygon[0], polygon[-1]))
    
       
    # in case of entire polygon is on the left
    if max_x < point_x:
        return False
    
    # in case checking point is the same as in polygon    
    for points in polygon:
        if point_x == points[0] and point_y == points[1]:
            return True
            
    for curr_line in all_lines:
        size_x = sorted((curr_line[0][0], curr_line[1][0]))
        size_y = sorted((curr_line[0][1], curr_line[1][1]))
        
        if point_x == curr_line[0][0] == curr_line[1][0] and point_y in range(size_y[0], size_y[1]):
            return True
            
        elif point_y == curr_line[0][1] == curr_line[1][1] and point_x in range(size_x[0], size_x[1]):
            return True
            
        elif point_y in range(size_y[0], size_y[1]):
            result = two_lines(point2line, curr_line)
            
            if result[0] >= point_x and result not in cross_points:
                first, second = result
                result = (round(first), round(second))
                
                if list(result) not in polygon:
                    cross_points.append(result)
                    crossing += 1
                    
    result = crossing % 2
    
    return bool(result)
