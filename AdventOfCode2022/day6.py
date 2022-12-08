DATA_FILE = "./AdventOfCode2022/data/day6.txt"

def read_data():
    with open(DATA_FILE, "r") as f:
        return f.read().strip() 

def is_valid_marker(s):
    if not len(s) == 4:
        return False
    for i in range(0, len(s)-1):
        if s[i] in s[i+1:]:
            return False
    return True
   
def is_valid_marker2(s, marker_length):
    if not len(s) == marker_length:
        return False
    for i in range(0, len(s)-1):
        if s[i] in s[i+1:]:
            return False
    return True

def part1():
    data = read_data()

    for i in range(0, len(data)):
        if is_valid_marker(data[i:i+4]):
            print('at %s found valid marker %s' % (i+4, data[i:i+4]))
            return

def part2():
    data = read_data()

    for i in range(0, len(data)):
        if is_valid_marker2(data[i:i+14], 14):
            print('at %s found valid marker %s' % (i+14, data[i:i+14]))
            return



if __name__ == "__main__":

    print("==== starting day 3 part 1")
    part1()

    print("==== starting day 3 part 2")
    part2()

    print("==== done")
