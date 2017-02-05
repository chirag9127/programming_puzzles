"""
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0'
(the number zero), return the maximum enemies you can kill using one bomb.
"""


def bomb_enemy(grid):
    max_enemy = 0
    count = [[0 for j in xrange(len(grid[0]))] for i in xrange(len(grid))]
    for i in xrange(len(grid)):
        left_count = 0
        for j in xrange(len(grid[0])):
            count[i][j] += left_count
            left_count = get_count(grid[i][j], left_count)
        right_count = 0
        for j in xrange(len(grid[0]) - 1, -1, -1):
            count[i][j] += right_count
            right_count = get_count(grid[i][j], right_count)
    for j in xrange(len(grid[0])):
        down_count = 0
        for i in xrange(len(grid)):
            count[i][j] += down_count
            down_count = get_count(grid[i][j], down_count)
        up_count = 0
        for i in xrange(len(grid) - 1, -1, -1):
            count[i][j] += up_count
            up_count = get_count(grid[i][j], up_count)
    for i in xrange(len(grid)):
        for j in xrange(len(grid[0])):
            if grid[i][j] == '0':
                max_enemy = max(count[i][j], max_enemy)
    return max_enemy


def get_count(item, count):
    if item == 'E':
        return count + 1
    if item == 'W':
        return 0
    return count


def test_bomb_enemy():
    data = [['0', 'E', '0', '0'],
            ['E', '0', 'W', 'E'],
            ['0', 'E', '0', '0']]
    assert bomb_enemy(data) == 3
