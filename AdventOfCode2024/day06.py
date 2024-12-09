from collections import defaultdict
from bisect import insort, bisect
from itertools import cycle

DATA_FILE = "./AdventOfCode2024/data/day06.txt"

def part1(puzzle_input):
    grid = puzzle_input.split('\n')
    height, width = len(grid), len(grid[0])
    for i in range(height):
        for j in range(width):
            if grid[i][j] == '^':
                r, c = i, j

    direction = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
    d = next(direction)
    visited = set([(r, c)])
    while True:
        new_r = r + d[0]
        new_c = c + d[1]
        if new_r not in range(height) or new_c not in range(width):
            break 
        if grid[new_r][new_c] == '#':
            d = next(direction)
        else:
            r, c = new_r, new_c
            visited.add((r, c))

    return len(visited)

def part2(puzzle_input):
    grid = puzzle_input.split('\n')
    m, n = len(grid), len(grid[0])
    obstacles = {
        'rows': defaultdict(list),
        'cols': defaultdict(list),
    }
    for r in range(m):
        for c in range(n):
            if grid[r][c] == '#':
                insort(obstacles['rows'][r], c)
                insort(obstacles['cols'][c], r)
            if grid[r][c] == '^':
                start = (r, c, 'up')

    def move(r, c, d, obstacles):
        r_obs = obstacles['rows'][r]
        c_obs = obstacles['cols'][c]

        if d == 'up':
            if not c_obs or c_obs[0] > r:
                new_r = -1
            else:
                i = bisect(c_obs, r)
                new_r = c_obs[i-1] + 1
            return new_r, c, 'right'

        if d == 'right':
            if not r_obs or r_obs[-1] < c:
                new_c = n
            else:
                i = bisect(r_obs, c)
                new_c = r_obs[i] - 1
            return r, new_c, 'down'
        
        if d == 'down':
            if not c_obs or c_obs[-1] < r:
                new_r = m
            else:
                i = bisect(c_obs, r)
                new_r = c_obs[i] - 1
            return new_r, c, 'left'

        if d == 'left':
            if not r_obs or r_obs[0] > c:
                new_c = -1
            else:
                i = bisect(r_obs, c)
                new_c = r_obs[i-1] + 1
            return r, new_c, 'up'

    candidates = set()
    r, c, d = start
    while r in range(m) and c in range(n):
        new_r, new_c, new_d = move(r, c, d, obstacles)
        if d == 'up':
            candidates |= set((i, c) for i in range(new_r+1, r+1))
        elif d == 'right':
            candidates |= set((r, j) for j in range(c, new_c))
        elif d == 'down':
            candidates |= set((i, c) for i in range(r, new_r))
        elif d == 'left':
            candidates |= set((r, j) for j in range(new_c+1, c+1))
        r, c, d = new_r, new_c, new_d

    def is_looping(obstacles):
        r, c, d = start
        visited = set([start])
        while r in range(m) and c in range(n):
            r, c, d = move(r, c, d, obstacles)
            if (r, c, d) in visited:
                return True
            visited.add((r, c, d))
        return False
    
    loop_count = 0
    for r, c in candidates:
        insort(obstacles['rows'][r], c)
        insort(obstacles['cols'][c], r)
        loop_count += is_looping(obstacles)
        obstacles['rows'][r].remove(c)    
        obstacles['cols'][c].remove(r)

    return loop_count

if __name__ == "__main__":

    input_str = ''
    with open(DATA_FILE, 'r') as file:
        input_str = file.read()

    print("==== starting day 1 part 1")
    num_visited = part1(input_str)
    print("num visited: %s" % num_visited)

    print("==== starting day 1 part 2")
    num_loops = part2(input_str)
    print("num loops: %s" % num_loops)

    print("==== done")

