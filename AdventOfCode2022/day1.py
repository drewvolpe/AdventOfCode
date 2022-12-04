from functools import reduce


def read_data():
    elves = []
    elf = []
    with open("./AdventOfCode2022/data/day1.txt", "r") as f:
        for line in f.readlines():
            if line == '\n' or line == '':
                elves.append(elf)
                elf = []
            else:
                elf.append(int(line))
        if elf:
            elves.append(elf)
    return elves


def part1():
    elves = read_data()
    print("Read in %s elves" % len(elves))

    cals_per_elf = []
    for elf in elves:
        cals_per_elf.append( reduce(lambda x, y: x+y, elf) )

    cals_per_elf.sort()

    sum = reduce(lambda x,y: x+y, [c for c in cals_per_elf[-3:]])
    print("Top 3 elves: %s" % sum)


if __name__ == "__main__":

    print("==== starting day 1 part 1")
    part1()

    print("==== done")
