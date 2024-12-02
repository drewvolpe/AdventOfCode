

DATA_FILE = "./AdventOfCode2024/data/day01.txt"

def read_data():
    l_list = []
    r_list = []

    with open(DATA_FILE, "r") as f:
        for line in f.readlines():
            print('line: %s' % line)
            l, r = line.strip().split('  ')
            l_list.append(int(l))
            r_list.append(int(r))

    return l_list, r_list

def part1():
    l_list, r_list = read_data()
    l_list.sort()
    r_list.sort()

    print('l_list: %s' % l_list[0:10])
    print('r_list: %s' % r_list[0:10])
    
    dif_sum = 0
    for i in range(len(l_list)):
        dif = 0
        if l_list[i] > r_list[i]:
            dif = l_list[i] - r_list[i]
        else:
            dif = r_list[i] - l_list[i]
        dif_sum += dif

    print('dif_sum: %s' % dif_sum)
    return dif_sum

def part2():
    l_list, r_list = read_data()
    l_list.sort()
    r_list.sort()

    total_score = 0
    for i_l in l_list:
        num = r_list.count(i_l)
        total_score += (num * i_l)

    print('total_score: %s' % total_score)
    return total_score

if __name__ == "__main__":

    print("==== starting day 1 part 1")
    part1()

    print("==== starting day 1 part 2")
    part2()

    print("==== done")


