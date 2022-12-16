import re

DATA_FILE = "./AdventOfCode2022/data/day8.txt"

def read_data():
    heights = []
    with open(DATA_FILE, "r") as f:
        for h in f.readlines():
            heights.append([int(x) for x in h.strip()])

    return heights

def part1():
    grid = read_data()

    grid_height = len(grid)
    grid_width = len(grid[0])
    print("grid: %s x %s " % (grid_height, grid_width))

    is_visible_arr = []
    for i in range(0, grid_height):
        is_visible_arr.append([])
        for j in range(0, grid_width):
            is_visible_arr[i].append(0)

    for i in range(0, grid_height):
        # down left side
        cur_max = -1
        for j in range(0, grid_width):
            cur_height = grid[i][j]
            if cur_height > cur_max:
                is_visible_arr[i][j] = 1
                cur_max = cur_height

        # down right side
        cur_max = -1
        for j in range(grid_width-1, -1, -1):
            cur_height = grid[i][j]
            if cur_height > cur_max:
                is_visible_arr[i][j] = 1
                cur_max = cur_height

    for j in range(0, grid_width):
        # top
        cur_max = -1
        for i in range(0, grid_height):
            cur_height = grid[i][j]
            if cur_height > cur_max:
                is_visible_arr[i][j] = 1
                cur_max = cur_height

        # bottom row
        cur_max = -1
        for i in range(grid_height-1, -1, -1):
            cur_height = grid[i][j]
            if cur_height > cur_max:
                is_visible_arr[i][j] = 1
                cur_max = cur_height

    print("=== is_visible_arr")
    for i in range(0, grid_height):
        print('%s' % is_visible_arr[i])

    print("=== GRID")
    for i in range(0, grid_height):
        print('%s' % grid[i])

    print("=== is_visible_arr")
    num_visible = 0
    for i in range(0, grid_height):
        print('%s' % is_visible_arr[i])
        num_visible += len([x for x in is_visible_arr[i] if x == 1])

    print('='*4)
    print("total visible: %s" % num_visible)

def part2():
    grid = read_data()

    grid_height = len(grid)
    grid_width = len(grid[0])
    print("grid: %s x %s " % (grid_height, grid_width))

    visibibility_arr = []
    for i in range(0, grid_height):
        visibibility_arr.append([])
        for j in range(0, grid_width):
            visibibility_arr[i].append(0)

    for i in range(0, grid_height):
        for j in range(0, grid_width):
            # look up
            cur_row = i-1
            cur_max_height = grid[i][j]
            while (cur_row > 0):
                if grid[cur_row][j] > cur_max_height:
                    visibibility_arr[i][j] += 1
                    cur_max_height = grid[cur_row][j]
                cur_row -= 1

            # look down
            cur_row = i+1
            cur_max_height = grid[i][j]
            while (cur_row < grid_height):
                if grid[cur_row][j] > cur_max_height:
                    visibibility_arr[i][j] += 1
                    cur_max_height = grid[cur_row][j]
                cur_row += 1

            # look right
            cur_col = j+1
            cur_max_height = grid[i][j]
            while (cur_col < grid_width):
                if grid[cur_col][j] > cur_max_height:
                    visibibility_arr[i][j] += 1
                    cur_max_height = grid[i][cur_col]
                cur_col += 1

            # look left
            cur_col = j-1
            cur_max_height = grid[i][j]
            while (cur_col > 0):
                if grid[cur_col][j] > cur_max_height:
                    visibibility_arr[i][j] += 1
                    cur_max_height = grid[i][cur_col]
                cur_col -= 1

    print("=== visibility_arr")
    for i in range(0, grid_height):
        print('%s' % visibibility_arr[i])

    highest_score = 0
    for i in range(0, grid_height):
        for j in range(0, grid_width):
            if grid[i][j] > highest_score:
                highest_score = grid[i][j]

    print("Highest score: %s" % highest_score)

if __name__ == "__main__":

    print("==== starting day 8 part 1")
    part1()

    print("==== starting day 8 part 2")
    part2()

    print("==== done")
