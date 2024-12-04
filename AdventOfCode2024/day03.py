import re

DATA_FILE = "./AdventOfCode2024/data/day03.txt"

def read_data():
    lines = []

    with open(DATA_FILE, "r") as f:
        for line in f.readlines():
            lines.append(line)
    return lines

def part1():
    lines = read_data()

    results_sum = 0
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    for line in lines:
        matches = re.findall(pattern, line)
        for a, b in matches:
            results_sum += (int(a) * int(b))
    
    print("results_sum: %s" % results_sum)
    return results_sum

def run_muls(str, start_pos, end_pos):
    cur_str = str[start_pos:end_pos]
    results_sum = 0
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, cur_str)
    for a, b in matches:
        results_sum += (int(a) * int(b))
    return results_sum

def part2():
    lines = read_data()
    data_str = ""
    for l in lines:
        data_str += l

    total_results_sum = 0
    cur_pos = 0
    in_do = True
    while (cur_pos < len(data_str)):
        if in_do:
            # collect muls until next don't
            next_dont = data_str.find("don't()", cur_pos)
            if next_dont < 0: # no more
                total_results_sum += run_muls(data_str, cur_pos, len(data_str))
                cur_pos = len(data_str)
            else:                 
                total_results_sum += run_muls(data_str, cur_pos, next_dont)
                cur_pos = next_dont + 7
                in_do = False
        else:
            # in don't, so jump ahead to next do
            next_do = data_str.find("do()", cur_pos)
            if next_do == -1:
                cur_pos = len(lines)
                continue
            cur_pos = next_do + 4
            in_do = True

    print("total_results_sum: %s" % total_results_sum)
    return total_results_sum


if __name__ == "__main__":

    print("==== starting day 1 part 1")
    part1()

    print("==== starting day 1 part 2")
    part2()

    print("==== done")


