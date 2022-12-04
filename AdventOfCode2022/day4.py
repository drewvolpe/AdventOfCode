from functools import reduce

DATA_FILE = "./AdventOfCode2022/data/day4.txt"

def read_data():
    datas = []
    with open(DATA_FILE, "r") as f:
        for line in f.readlines():
            a,b = line.strip().split(',')
            a = [int(x) for x in a.split('-')]
            b = [int(x) for x in b.split('-')]
            datas.append([a, b])
    return datas


def is_fully_contained(a1, a2, b1, b2):
    if ((a1 <= b1 and a2 >= b2) or
        (b1 <= a1 and b2 >= a2)):
        return True
    return False

def part1():
    elves = read_data()
    num_contained = 0
    for e1, e2 in elves:
#        print("        elves: %s %s " % (e1, e2))
        if is_fully_contained(e1[0], e1[1], e2[0], e2[1]):
            num_contained += 1
#            print("    contained: %s %s " % (e1, e2))
    print("Num contained: %s" % num_contained)


def is_any_overlap(a1, a2, b1, b2):
    if ((a1 <= b2 and a2 >= b2) or
        (b1 <= a2 and b2 >= a2)):
        return True
    return False

def part2():
    elves = read_data()
    num_overlap = 0
    for e1, e2 in elves:
#        print("        elves: %s %s " % (e1, e2))
        if is_any_overlap(e1[0], e1[1], e2[0], e2[1]):
            num_overlap += 1
#            print("    overlap: %s %s " % (e1, e2))
    print("Num overlap: %s" % num_overlap)


if __name__ == "__main__":

    print("==== starting day 3 part 1")
    part1()

    print("==== starting day 3 part 2")
    part2()

    print("==== done")

