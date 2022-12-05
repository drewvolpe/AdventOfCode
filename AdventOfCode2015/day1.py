from functools import reduce

def read_data():
    with open("./AdventOfCode2015/data/day1.txt", "r") as f:
        all_parens_str = ''
        for line in f.readlines():
            all_parens_str = all_parens_str + line.strip()
    return all_parens_str

def part1():
    all_parens_str = read_data()
    num_left = len([x for x in all_parens_str if x == '('])
    num_right = len([x for x in all_parens_str if x == ')'])
    floors = num_left - num_right    

    print('total floors: %s' % floors)

def part2():
    all_parens_str = read_data()
    cur_floor = 0
    for cur_pos in range(0, len(all_parens_str)):
        chg = 1 if all_parens_str[cur_pos] == '(' else -1
        cur_floor += chg
        if cur_floor == -1:
            print('In basement at position: %s' % (cur_pos+1))
            break
    

if __name__ == "__main__":

    print("==== starting day 1 part 1")
    part1()

    print("==== starting day 1 part 2")
    part2()

    print("==== done")
