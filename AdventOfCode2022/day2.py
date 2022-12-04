from functools import reduce

DATA_FILE = "./AdventOfCode2022/data/day2.txt"

def read_data1():
    rounds = []
    with open(DATA_FILE, "r") as f:
        for line in f.readlines():
            line = line.strip().replace('A', 'R').replace('X', 'R')
            line = line.replace('B', 'P').replace('Y', 'P')
            line = line.replace('C', 'S').replace('Z', 'S')
            rounds.append(line.split(' '))
    return rounds

def read_data2():
    rounds = []
    with open(DATA_FILE, "r") as f:
        for line in f.readlines():
            line = line.strip().replace('A', 'R').replace('X', 'L')
            line = line.replace('B', 'P').replace('Y', 'D')
            line = line.replace('C', 'S').replace('Z', 'W')
            rounds.append(line.split(' '))
    return rounds


def round_result(round):
    winners = [['R', 'P'], ['P', 'S'], ['S', 'R']] # hands player wins
    losers = [[y, x] for (x, y) in winners]
    if (round in winners):
        return 1
    elif (round in losers):
        return -1
    return 0

def part1():
    rounds = read_data1()

    win_loss_points = 0
    shape_points = 0
    for r in rounds:
        result = round_result(r)
        if (result == 0):
            win_loss_points += 3
        elif (result > 0):
            win_loss_points += 6

    # 1 for rocks played, 2 for papers played, 3 for scissors played
    player_shapes = [y for x,y in rounds]
    shape_points += (len([x for x in player_shapes if x == 'R']) * 1)
    shape_points += (len([x for x in player_shapes if x == 'P']) * 2)
    shape_points += (len([x for x in player_shapes if x == 'S']) * 3)

#    print('player shapes: %s ' % player_shapes)    
    print('win_loss_points: %s ' % win_loss_points)
    print('shape points: %s ' % shape_points)
    print('total points: %s' % (win_loss_points + shape_points))


def part2():
    rounds = read_data2()

    win_loss_points = 0
    player_shapes = []
    for round in rounds:
        x, result = round
        if result == 'D':
            y = x
            win_loss_points += 3

        elif result == 'W':
            win_loss_points += 6
            if x == 'R':
                y = 'P'
            elif x == 'P':
                y = 'S'
            else:
                y = 'R'
        elif result == 'L':
            if x == 'R':
                y = 'S'
            elif x == 'P':
                y = 'R'
            else:
                y = 'P'
        round = [x, y]
        player_shapes.append(y)

    # 1 for rocks played, 2 for papers played, 3 for scissors played
    shape_points = (len([x for x in player_shapes if x == 'R']) * 1)
    shape_points += (len([x for x in player_shapes if x == 'P']) * 2)
    shape_points += (len([x for x in player_shapes if x == 'S']) * 3)

#    print('player shapes: %s ' % player_shapes)    
    print('win_loss_points: %s ' % win_loss_points)
    print('shape points: %s ' % shape_points)
    print('total points: %s' % (win_loss_points + shape_points))


if __name__ == "__main__":

    print("==== starting day 2 part 1")
    part1()

    print("==== starting day 2 part 2")
    part2()

    print("==== done")

