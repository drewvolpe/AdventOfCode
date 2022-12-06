from functools import reduce

def read_data():
    the_strings = []
    with open("./AdventOfCode2015/data/day5.txt", "r") as f:
        the_strings = f.read().split('\n')

    return the_strings

def is_nice(s):
    # 3 vowels
    if len([x for x in s if x in 'aeiou']) < 3:
        return False

    # does not contain ab, cd, pq, or xy
    for a in ['ab', 'cd', 'pq', 'xy']:
        if a in s:
            return False

    # 1 letter 2x in a row
    last_c = s[0]
    for cur_c in s[1:]:
        if cur_c == last_c:
            return True
        last_c = cur_c
    return False

def part1():
    the_strings = read_data()
    print('Read in %s strings' % len(the_strings))

    nice_strings = []
    for x in the_strings:
        if is_nice(x):
            nice_strings.append(x)


    print('%s nice strings' % len(nice_strings))

def is_nice2(s):
    # pair of letters appears twice
    found_pair = False
    for i in range(0, len(s)-2):
        pair = s[i:i+2]
        if pair in s[i+2:]:
            found_pair = True
            break
    if not found_pair:
        return False

    # one letter which repeats with 1 letter between
    # xyx, efe, aaa, ...
    found_repeat = False
    for i in range(0, len(s)-2):
        if found_repeat:
            break
        c = s[i]
        for j in range(i+1, len(s)):
            if c == s[i+2]:
                found_repeat = True
                break
    if not found_repeat:
        return False
    return True

def part2():
    the_strings = read_data()
    print('Read in %s strings' % len(the_strings))

#    the_strings = ['qjhvhtzxzqqjkmpb','xxyxx','uurcxstgmygtbstg','ieodomkazucvgmuy']
    nice_strings = []
    for x in the_strings:
#        print("%s string: %s" % (is_nice2(x), x))
        if is_nice2(x):
            nice_strings.append(x)

    print('%s nice strings' % len(nice_strings))

if __name__ == "__main__":

    print("==== starting day 1 part 1")
    part1()

    print("==== starting day 1 part 2")
    part2()

    print("==== done")

