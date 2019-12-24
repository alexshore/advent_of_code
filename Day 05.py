
def intcode_processing(filename=None, a=0, b=0):
    lst = get_list(filename) if filename else [99]
    lst[1], lst[2] = a, b
    current_pos = 0
    while current_pos < len(lst):
        if lst[current_pos] == 1:
            lst[lst[current_pos + 3]] = lst[lst[current_pos + 1]] + lst[lst[current_pos + 2]]
        elif lst[current_pos] == 2:
            lst[lst[current_pos + 3]] = lst[lst[current_pos + 1]] * lst[lst[current_pos + 2]]
        elif lst[current_pos] == 99:
            return lst
        current_pos += 4
    return lst

def get_list(filename):
    f = open(filename, "r")
    lst = [int(i) for i in f.read().split(',')]
    f.close()
    return lst

def main():
    for a in range(0, 100):
        for b in range(0, 100):
            lst = intcode_processing("Day 02.txt", a, b)
            if lst[0] == 19690720:
                print((100 * a) + b)
            

if __name__ == '__main__':
    main()