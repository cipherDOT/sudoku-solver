grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def possible(y, x, n):
    for i in range(len(grid)):
        if grid[y][i] == n:
            return False
    for j in range(len(grid[0])):
        if grid[j][x] == n:
            return False

    xoff = (x // 3) * 3
    yoff = (y // 3) * 3

    for i in range(0, 3):
        for j in range(0, 3):
            if grid[yoff + i][xoff + j] == n:
                return False

    return True


def print_matrix(m):
    if m == None or m == []:
        print('No solution')
        return
    line = '----------------------'
    rows = len(m)
    cols = len(m[0])

    for i in range(rows):
        if i % 3 == 0:
            print(line)

        row_to_print = ""
        for j in range(cols):
            if j % 3 == 0:
                row_to_print += '|'
            value = str(m[i][j]) if m[i][j] > 0 else ' '
            row_to_print += value + " "
        row_to_print += '|'
        print(row_to_print)
    print(line)


def solve():
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print_matrix(grid)


solve()
