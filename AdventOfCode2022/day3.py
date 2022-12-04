from functools import reduce

DATA_FILE = "./AdventOfCode2022/data/day3.txt"

def read_data():
    sacks = []
    with open(DATA_FILE, "r") as f:
        for line in f.readlines():
            line = line.strip()
            halfway = round(len(line)/2)
            sacks.append([line[0:halfway], line[halfway:]])
    return sacks


def read_data2():
    sacks = []
    with open(DATA_FILE, "r") as f:
        for line in f.readlines():
            sack = line.strip()
            if sack:
                sacks.append(sack)
    return sacks


def part1():
    sacks = read_data()

    # find items in both sides
    dupes = []    
    for s in sacks:
        cur_dupes = set(s[0]).intersection(s[1])        
        dupes.extend(cur_dupes)

#    print("dupes: %s" % dupes)
    print('found %s dupes' % len(dupes))

    dupe_vals = []
    for d in dupes:
        v = ord(d)
        if v >= 97:  # 'a'
            v -= 96
        else:
            v -= 38  # 'A'
        dupe_vals.append(v)

    total = reduce(lambda x,y: x+y, dupe_vals)
    print("total: %s" % total)


def part2():
    sacks = read_data2()

    badges = []
    for x in range(0, len(sacks), 3):
        a,b,c = sacks[x:x+3]
        badge = set(a).intersection(b).intersection(c).pop()
        badges.append(badge)
    
    print('found %s badges' % len(badges))

    badge_vals = []
    for b in badges:
        v = ord(b)
        if v >= 97:  # 'a' in ascii
            v -= 96
        else:
            v -= 38  # 'A'
        badge_vals.append(v)

    total = reduce(lambda x,y: x+y, badge_vals)
    print("total: %s" % total)


if __name__ == "__main__":

    print("==== starting day 3 part 1")
    part1()

    print("==== starting day 3 part 2")
    part2()

    print("==== done")

