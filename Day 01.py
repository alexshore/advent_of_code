
def total_weight():
    f = open("01.01.txt", "r")
    total = sum([fuel_for_module(i) for i in [int(each) for each in f.read().split('\n')]])
    f.close()
    return total

def fuel_for_module(weight):
    fuel = int(weight / 3) - 2
    if fuel <= 0:
        return 0
    return fuel + fuel_for_module(fuel)

if __name__ == '__main__':
    print(total_weight())
    