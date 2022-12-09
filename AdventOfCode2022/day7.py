from collections import defaultdict
import re

DATA_FILE = "./AdventOfCode2022/data/day7.txt"

def read_data():
    commands = []
    with open(DATA_FILE, "r") as f:
        commands = f.readlines()
    return commands

def create_sizes_dict():
    commands = read_data()

    sizes_dict = defaultdict(int)
    path = []
    numbers = ("^\d+")

    for command in commands:
        if command.startswith("$ cd"):
            d = command.split()[-1]
            if d == '..':
                path.pop()
                print("Up to %s" % path)
            else:
                if d == "/":
                    path.append("root")
                else:
                    path.append(d)
                    print("Into %s" % path)
        elif re.match(numbers, command):
            print("File: %s" % command)
            size, _ = command.split()
            if re.match(numbers, size): # I know it'S dumb 
                for i in range(len(path)):
                    sizes_dict
                    sizes_dict["/".join(path[:i+1])] += int(size)
    return sizes_dict

def part1():
    sizes_dict = create_sizes_dict()

    total_size = 0
    for k, v in sizes_dict.items():
        if v < 100000:
            total_size += v
    print("Total size: %s" % total_size)

def part2():
    sizes_dict = create_sizes_dict()

    root_size = sizes_dict['root']
    print('root size: %s' % root_size)

    total_space = 70000000
    free_space = total_space - root_size
    needed_space = 30000000 - free_space

    cur_best = total_space
    for k, v in sizes_dict.items():
        if v >= needed_space and v < cur_best:
            cur_best = v
    print("min size: %s" % cur_best)

if __name__ == "__main__":

    print("==== starting day 7 part 1")
    part1()

    print("==== starting day 7 part 2")
    part2()

    print("==== done")
