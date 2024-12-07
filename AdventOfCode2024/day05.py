from collections import defaultdict
import re

DATA_FILE = "./AdventOfCode2024/data/day05.txt"

def read_data():
    rules = []
    updates_list = []
    is_rules = True
    with open(DATA_FILE, "r") as f:
        for line in f.readlines():
            if line.strip() == '':
                is_rules = False
                continue
            if is_rules:
                rules.append([int(x) for x in line.split('|')])
            else:
                updates_list.append([int(x) for x in line.split(',')])

    return rules, updates_list


def did_rule_pass(rule, updates):
    left_pos = -1
    right_pos = -1
    try:
        left_pos = updates.index(rule[0])
        right_pos = updates.index(rule[1])
    except ValueError:
        return True
    if left_pos > right_pos:
        return False
    return True


def part1():
    rules, updates_list = read_data()
    print("found %s rules and %s updates" % (len(rules), len(updates_list)))

    sum = 0
    for up in updates_list:
        rule_passed = True
        for rule in rules:
            if not did_rule_pass(rule, up): 
                rule_passed = False
        if rule_passed:
            sum += up[len(up)//2]
    print("sum %s" % sum)
    return sum

def part2():

    input_str = ''
    with open(DATA_FILE, 'r') as file:
        input_str = file.read()

    rules, updates = input_str.split('\n\n')
    print("rules: %s" % rules)
    print("updates: %s" % updates)

    preceding = defaultdict(set)
    for p1, p2 in re.findall(r'(\d+)\|(\d+)', rules):
        preceding[int(p2)].add(int(p1))

    def get_score(pages, is_reordered=False):
        disallowed_after = dict()
        for i, page in enumerate(pages):
            if page in disallowed_after:
                j = disallowed_after[page]
                reordered = pages[:j] + [page] + pages[j:i] + pages[i+1:]
                return get_score(reordered, True)
            
            for p in preceding[page]:
                if p not in disallowed_after:
                    disallowed_after[p] = i
            
        return pages[len(pages)//2] if is_reordered else 0

    sum = 0
    for line in updates.split('\n'):
        pages = list(map(int, line.split(',')))
        sum += get_score(pages)

    print("sum: %s" % sum)
    return sum


if __name__ == "__main__":

    print("==== starting day 1 part 1")
    part1()

    print("==== starting day 1 part 2")
    part2()

    print("==== done")

