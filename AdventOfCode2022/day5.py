from functools import reduce
import re

DATA_FILE = "./AdventOfCode2022/data/day5.txt"

def read_data():
    rows = []
    moves = []
    num_cols = None
    with open(DATA_FILE, "r") as f:
        for line in f.readlines():
            cur_cols = []
            if '[' in line:
                if not num_cols:
                    num_cols = int((len(line) + 1)/4)
#                    print('num cols: %s' % num_cols)
#                print('line: "%s"' % line)
                for i in range(0, num_cols):
                    cur_cols.append(line[1 + (i*4)]) # assume fixed width
                rows.append( cur_cols )
            elif line.startswith('move'):
                moves.append([int(x) for x in re.findall('\d+', line)])


    cols = []
    for x in range(0, num_cols):
        c = []
        for r in rows:
            if r[x].strip():
                c.append(r[x])
        c.reverse()
        cols.append(c)

    return cols, moves


def part1():
    cols, moves = read_data()

    for m in moves:
        a = m[1]
        b = m[2]
        num_crates = m[0]
        for i in range(0, num_crates):
            cols[b-1].append(cols[a-1].pop())

#    print(' final cols:')
#    print(' cols: %s ' % (cols))

    print('')
    print(' tops: %s' % [x[-1] for x in cols])


def part2():
    cols, moves = read_data()

    for m in moves:
        a = m[1]
        b = m[2]
        num_crates = m[0]

        crates_to_add = []
        for i in range(0, num_crates):
            crates_to_add.append(cols[a-1].pop())
        crates_to_add.reverse()
        for c in crates_to_add:
            cols[b-1].append(c)

    print('')
    print(' tops: %s' % [x[-1] for x in cols])


if __name__ == "__main__":

    print("==== starting day 3 part 1")
    part1()

    print("==== starting day 3 part 2")
    part2()

    print("==== done")
