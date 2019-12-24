
def calc_wire_path(path):
    cur_x = cur_y = step = 0
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    points = dict()
    for segment in path:
        d_x, d_y = directions[segment[0]]
        for _ in range(int(segment[1:])):
            cur_x += d_x
            cur_y += d_y
            step += 1
            if (cur_x, cur_y) not in points:
                points[(cur_x, cur_y)] = step

    return points

f = open("Day 03.txt", "r")
wire1_path, wire2_path = f.read().split('\n')

wire1_points = calc_wire_path(wire1_path.split(','))
wire2_points = calc_wire_path(wire2_path.split(','))

intersection_points = [point for point in wire1_points if point in wire2_points]
print(min(abs(x) + abs(y) for (x, y) in intersection_points))
print(min(wire1_points[point] + wire2_points[point] for point in intersection_points))