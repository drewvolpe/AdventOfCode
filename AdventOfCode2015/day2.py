from functools import reduce

def read_data():
    with open("./AdventOfCode2015/data/day2.txt", "r") as f:
        presents = []
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            presents.append( [int(x) for x in line.split('x')] )
    return presents

def compute_paper_needed(l, w, h):
    s1 = (l*w)
    s2 = (w*h)
    s3 = (h*l)
    l = [s1, s2, s3]
    l.sort()

    return 2*s1 + 2*s2 + 2*s3 + l[0]


def part1():
    presents = read_data()

    total_paper = 0
    for p in presents:
        total_paper += compute_paper_needed(p[0], p[1], p[2])
    print("total: %s" % total_paper)

def compute_ribbon_needed(l, w, h):
    sides = [l, w, h]
    sides.sort()

    return 2*sides[0] + 2*sides[1] + (l*w*h)

def part2():
    presents = read_data()

    total_ribbon = 0
    for p in presents:
        total_ribbon += compute_ribbon_needed(p[0], p[1], p[2])
        
    print("total ribbon: %s" % total_ribbon)

    

if __name__ == "__main__":

    print("==== starting day 1 part 1")
    part1()

    print("==== starting day 1 part 2")
    part2()

    print("==== done")

