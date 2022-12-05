from functools import reduce
import hashlib


def parts(start_str):
    key = 'yzbqklnj'
    result = hashlib.md5(key.encode('utf-8'))

    print('hex: %s' % result.hexdigest())

    cur_num = 0
    while (True):
        cur_str = key + str(cur_num)
        result = hashlib.md5(cur_str.encode('utf-8'))
        the_hash = result.hexdigest()

#        print('%s from %s' % (the_hash, cur_str))

        if the_hash.startswith(start_str):
            print('%s from %s' % (the_hash, cur_num))
            return

        cur_num += 1


def part2():
    pass


if __name__ == "__main__":

    print("==== starting day 1 part 1")
    parts('0'*5)

    print("==== starting day 1 part 2")
    parts('0'*6)

    print("==== done")

