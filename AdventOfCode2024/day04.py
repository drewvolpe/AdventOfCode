import re

DATA_FILE = "./AdventOfCode2024/data/day04.txt"

def read_data():
    lines = []
    with open(DATA_FILE, "r") as f:
        for line in f.readlines():
            lines.append(line)
    return lines

def find_xmas_in_str(line):
    num_found = line.count("XMAS")
    num_found += line.count("SAMX")
    return num_found

def check_right(lines, c, r):
    if c > len(lines[r])-4:
        return False
    l = lines[r]
    the_str = l[c] + l[c+1] + l[c+2] + l[c+3]
    if the_str == 'XMAS' or the_str == 'SAMX':
        return True
    return False

def check_down(lines, c, r):
    if r > (len(lines)-4):
        return False

    the_str = lines[r][c] + lines[r+1][c] + lines[r+2][c] + lines[r+3][c]
    if the_str == 'XMAS' or the_str == 'SAMX':
        return True
    return False

def check_diag_right(lines, c, r):
    if r > (len(lines)-4) or c > len(lines[r])-4:
        return False   

    the_str = lines[r][c] + lines[r+1][c+1] + lines[r+2][c+2] + lines[r+3][c+3]
    if the_str == 'XMAS' or the_str == 'SAMX':
        return True
    return False

def check_diag_left(lines, c, r):
    if r > (len(lines)-4) or c < 3:
        return False   

    the_str = lines[r][c] + lines[r+1][c-1] + lines[r+2][c-2] + lines[r+3][c-3]
    if the_str == 'XMAS' or the_str == 'SAMX':
        return True
    return False

def part1():
    num_total = 0
    lines = read_data()

    for c in range(0, len(lines[0])):
        for r in range(0, len(lines)):
            if check_right(lines, c, r):
                num_total += 1
            if check_down(lines, c, r):
                num_total += 1
            if check_diag_left(lines, c, r):
                num_total += 1
            if check_diag_right(lines, c, r):
                num_total += 1

    print("num_total: %s" % num_total)
    return num_total


def check_mas(lines, c, r):
    if lines[r][c] != 'M':
        return False
    

def part2():
    num_total = 0
    rows = read_data()

    height = len(rows)
    width = len(rows[0])

    def check(r, c):
        if rows[r][c] != 'A':
            return False
        ul = rows[r-1][c-1]
        ur = rows[r-1][c+1]
        dl = rows[r+1][c-1]
        dr = rows[r+1][c+1]
        return sorted([ul, ur, dl, dr]) == ['M', 'M', 'S', 'S'] and ul != dr
    
    num_total = sum(check(r, c) for r in range(1, height-1) for c in range(1, width-1))
    print("num_total: %s" % num_total)
    return num_total

if __name__ == "__main__":

    print("==== starting day 1 part 1")
    part1()

    print("==== starting day 1 part 2")
    part2()

    print("==== done")

