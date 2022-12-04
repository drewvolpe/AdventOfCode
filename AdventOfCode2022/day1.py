from functools import reduce

def read_data():
    elves = []
    elf = []
    with open("./data/day1.txt", "r") as f:
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

    for elf in elves:
        print("%s " % elf)

    cals_per_elf = []
    for elf in elves:
        cals_per_elf.append( reduce(lambda x, y: x+y, elf) )

    cals_per_elf.sort()
    print("Top elves:")
    sum = 0
    for c in cals_per_elf[-3:]:
        print("cal: %s" % c)
        sum += c
    print("sum: %s" % sum)


if __name__ == "__main__":

    print("==== starting day 1 part 1")
    part1()

    print("==== done")
