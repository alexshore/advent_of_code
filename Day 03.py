
START = 1

def plot_path(lst, matrix, intersections):
    pos_x = pos_y = 1
    matrix[pos_x][pos_y] = "o"
    for item in lst:
        if item[0] == "R":
            for _ in range(int(item[1:])):
                pos_x += 1
                if matrix[pos_x][pos_y] in ['-', '|', 'X', '+']:
                    matrix[pos_x][pos_y] = 'X'
                    if (pos_x, pos_y) not in intersections:
                        intersections.append((pos_x, pos_y))
                else:
                    matrix[pos_x][pos_y] = '-'
        elif item[0] == "L":
            for _ in range(int(item[1:])):
                pos_x -= 1
                if matrix[pos_x][pos_y] in ['-', '|', 'X', '+']:
                    matrix[pos_x][pos_y] = 'X'
                    if (pos_x, pos_y) not in intersections:
                        intersections.append((pos_x, pos_y))
                else:
                    matrix[pos_x][pos_y] = '-'
        elif item[0] == "U":
            for _ in range(int(item[1:])):
                pos_y += 1
                if matrix[pos_x][pos_y] in ['-', '|', 'X', '+']:
                    matrix[pos_x][pos_y] = 'X'
                    if (pos_x, pos_y) not in intersections:
                        intersections.append((pos_x, pos_y))
                else:
                    matrix[pos_x][pos_y] = '|'
        elif item[0] == "D":
            for _ in range(int(item[1:])):
                pos_y -= 1
                if matrix[pos_x][pos_y] in ['-', '|', 'X', '+']:
                    matrix[pos_x][pos_y] = 'X'
                    if (pos_x, pos_y) not in intersections:
                        intersections.append((pos_x, pos_y))
                else:
                    matrix[pos_x][pos_y] = '|'
        matrix[pos_x][pos_y] = '+'

def quick_print(matrix):
    output = ""
    for i in range(len(matrix)):
        row = ""
        for j in range(len(matrix[0])):
            row += matrix[j][i] + " "
        output = row + '\n' + output
    print(output)

def find_closest_intersection(intersections):
    return min([abs((i[0] - START) + (i[1] - START)) for i in intersections])

def main():
    lst1 = ["R8","U5","L5","D3"]
    lst2 = ["U7","R6","D4","L4"]
    matrix = [["." for _ in range(10)] for _ in range(10)]
    intersections = []
    quick_print(matrix)
    plot_path(lst1, matrix, intersections)
    quick_print(matrix)
    plot_path(lst2, matrix, intersections)
    quick_print(matrix)
    print(find_closest_intersection(intersections))

if __name__ == '__main__':
    main()