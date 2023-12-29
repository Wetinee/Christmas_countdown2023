def parse(data):
    matrix = [list(line) for line in data]
    return (matrix, len(matrix[0]), len(matrix))

def calculate_with_weight(data, weight):
    matrix, width, height = parse(data)
    row_distances = [1 if '#' in matrix[y] else weight for y in range(height)]
    column_distances = [1 if '#' in [matrix[y][x] for y in range(height)] else weight for x in range(width)]
    galaxy_poses = [(x, y) for x in range(width) for y in range(height) if matrix[y][x] == '#']
    distance_sum = 0
    for i in range(len(galaxy_poses)):
        for j in range(i, len(galaxy_poses)):
            (x1, y1), (x2, y2) = galaxy_poses[i], galaxy_poses[j]
            min_x, min_y, max_x, max_y = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2) # manhantan distance
            distance_sum += sum(row_distances[min_y:max_y]) + sum(column_distances[min_x:max_x])
    return distance_sum

def q1():
    return calculate_with_weight(data, 2)

def q2():
    return calculate_with_weight(data, 1_000_000)
