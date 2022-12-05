from functools import reduce

def read_data():
    with open("./AdventOfCode2015/data/day3.txt", "r") as f:
        moves_str = f.read()
    return [x for x in moves_str]

def do_move(m, x,y):
    if m == '^':
        y += 1
    elif m == 'v':
        y -= 1
    elif m == '>':
        x += 1
    elif m == '<':
        x -= 1
    else:
        raise Exception('unknown move: %s' % m)
    return (x, y)

def part1():
    moves = read_data()
    print('read in %s moves' % len(moves))

    visited = [(0,0)]
    x, y = (0,0)
    for m in moves:
        x, y = do_move(m, x, y)
        visited.append( (x,y) )
    
    print('Made %s visits' % len(visited))
    visited_set = set(visited)

    print('%s houses got 1+ visits' % len(visited_set))

def part2():
    moves = read_data()
    print('read in %s moves' % len(moves))
    
    santa_moves = []
    robot_moves = []
    for i in range(0, len(moves), 2):
        santa_moves.append(moves[i])
        robot_moves.append(moves[i+1])

    print('%s santa moves %s robot moves ' % (len(santa_moves), len(robot_moves)))

    santa_visited = [(0,0)]
    x,y = (0,0)
    for m in santa_moves:
        x,y = do_move(m, x, y)
        santa_visited.append( (x,y) )

    robot_visited = [(0,0)]
    x,y = (0,0)
    for m in robot_moves:
        x,y = do_move(m, x, y)
        robot_visited.append( (x,y) )
    
    all_visited = santa_visited
    all_visited.extend(robot_visited)
    visited_set = set(all_visited)

    print('%s houses got 1+ visits' % len(visited_set))

    # 933 is too low


if __name__ == "__main__":

    print("==== starting day 1 part 1")
    part1()

    print("==== starting day 1 part 2")
    part2()

    print("==== done")

