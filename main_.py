import random
import os

ROWS = 15
COLS = 55

WALL = '█'
EMPTY = ' '
EXIT = 'E'

maze = []


def draw_maze():
    os.system('cls')
    for row in maze:
        print(*row, sep='')


def check_maze():
    for row_idx, row in enumerate(maze):
        for col_idx, col in enumerate(row):
            if row_idx % 2 == 0 and col_idx % 2 == 0:
                if col == WALL:
                    return False
    return True


def make_frame():
    maze.insert(0, [WALL] * (COLS))
    maze.append([WALL] * (COLS))
    for row in maze:
        row.insert(0, WALL)
        row.append(WALL)


for row_idx in range(ROWS):
    row = []
    for col_idx in range(COLS):
        row.append(WALL)
    maze.append(row)

bulldozer_col = random.choice(range(0, COLS, 2))
bulldozer_row = random.choice(range(0, ROWS, 2))

maze[bulldozer_row][bulldozer_col] = 'a'

while not check_maze():  # остановить цикл когда сломаны все четные
    bulldozer_direction = []
    if bulldozer_col + 2 <= COLS:
        bulldozer_direction.append('right')
    if bulldozer_col - 2 >= 0:
        bulldozer_direction.append('left')
    if bulldozer_row + 2 <= ROWS:
        bulldozer_direction.append('down')
    if bulldozer_row - 2 >= 0:
        bulldozer_direction.append('up')

    if not bulldozer_direction:
        print('a')
        break

    direction = random.choice(bulldozer_direction)
    if direction == 'right':
        if maze[bulldozer_row][bulldozer_col + 2] == WALL:
            maze[bulldozer_row][bulldozer_col + 1] = EMPTY
            maze[bulldozer_row][bulldozer_col + 2] = EMPTY
        bulldozer_col += 2
    if direction == 'left':
        if maze[bulldozer_row][bulldozer_col - 2] == WALL:
            maze[bulldozer_row][bulldozer_col - 1] = EMPTY
            maze[bulldozer_row][bulldozer_col - 2] = EMPTY
        bulldozer_col -= 2
    if direction == 'up':
        if maze[bulldozer_row - 2][bulldozer_col] == WALL:
            maze[bulldozer_row - 1][bulldozer_col] = EMPTY
            maze[bulldozer_row - 2][bulldozer_col] = EMPTY
        bulldozer_row -= 2
    if direction == 'down':
        if maze[bulldozer_row + 2][bulldozer_col] == WALL:
            maze[bulldozer_row + 1][bulldozer_col] = EMPTY
            maze[bulldozer_row + 2][bulldozer_col] = EMPTY
        bulldozer_row += 2

    # print(check_maze())


make_frame()

maze[0][COLS] = EXIT
draw_maze()
