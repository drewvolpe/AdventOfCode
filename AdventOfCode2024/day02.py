
DATA_FILE = "./AdventOfCode2024/data/day02.txt"

def read_data():
    lines = []

    with open(DATA_FILE, "r") as f:
        for line in f.readlines():
            lines.append( [int(x) for x in line.strip().split(' ')] )

    return lines

def is_safe(line):
    is_inc = False
    if line[0] < line[1]:
        is_inc = True

    for i in range(0, len(line)-1):
        a = line[i]
        b = line[i+1]
        if a == b:
            return False
        
        # all inc or all decreasing
        if is_inc and a > b:
            return False
        elif not is_inc and a < b:
            return False
        
        # at most 3 diff
        if abs(a - b) > 3:
            return False


    return True

def part1():
    lines = read_data()
    print("read in %s lines " % len(lines))
    num_safe = 0
    for line in lines:
        print("%s - %s" % (is_safe(line), line))
        if is_safe(line):
            num_safe += 1

    print("num_safe: %s" % num_safe)
    return num_safe

def is_safe_w_damper(line):
    if is_safe(line):
        return True
    for i in range(0, len(line)):
        cur_line = line[0:i] + line[i+1:]
        if is_safe(cur_line):
            return True
    return False
                   
def part2():
    lines = read_data()
#    print("read in %s lines " % len(lines))
    num_safe = 0
    for line in lines:
        print("%s - %s" % (is_safe(line), line))
        if is_safe_w_damper(line):
            num_safe += 1

    print("num_safe: %s" % num_safe)
    return num_safe


if __name__ == "__main__":

    print("==== starting day 1 part 1")
    part1()

    print("==== starting day 1 part 2")
    part2()

    print("==== done")


