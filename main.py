'''
список списков
[
    [w], [e],
    [], [],
]
1 полностью заполнить стенами
2 количество колонн и рядов нечетное
3 бульдозер начинает в четной клетке
4 если в 2-х клетках от него стены - тогда ломает обе
5 лабиринт проходим, когда в четных клетках нет стен
6 внутренний лабиринт очертить границами - стенами
7 все четные клетки свободны выход (0(ряд), любая четная клетка)
'''
import random


COLS = 7
ROWS = 7
WALL = '█'
EMPTY = ' '
maze = []


def fill_map() -> None:
    for i in range(COLS * ROWS):
        maze.append([WALL])


def check_maze() -> bool:
    for i in range(0, len(maze), 2):
        if maze[i] == WALL:
            return False
    return True


def get_list_pos(col, row) -> int:
    return col + row * COLS


def break_walls() -> None:
    # (1, 0) 1-col, 0-row
    pos = (0, 0)
    while True:
        directions = []
        if pos[0] - 2 > 0:
            directions.append('left')
        if pos[1] - 2 > 0:
            directions.append('up')
        if pos[0] + 2 < COLS:
            directions.append('right')
        if pos[1] + 2 < ROWS:
            directions.append('down')

        direction = random.choice(directions)
        if direction == 'left':
            if maze[get_list_pos(pos[0] - 2, pos[1])] == '█':
                maze[get_list_pos(pos[0] - 1, pos[1])] = EMPTY
                maze[get_list_pos(pos[0] - 2, pos[1])] = EMPTY
                pos[0] -= 2
        elif direction == 'up':
            if maze[get_list_pos(pos[0], pos[1] - 2)] == '█':
                maze[get_list_pos(pos[0], pos[1] - 1)] = EMPTY
                maze[get_list_pos(pos[0], pos[1] - 2)] = EMPTY
                pos[1] -= 2
        elif direction == 'right':
            if maze[get_list_pos(pos[0] + 2, pos[1])] == '█':
                maze[get_list_pos(pos[0] + 1, pos[1])] = EMPTY
                maze[get_list_pos(pos[0] + 2, pos[1])] = EMPTY
                pos[0] += 2
        elif direction == 'down':
            if maze[get_list_pos(pos[0], pos[1] + 2)] == '█':
                maze[get_list_pos(pos[0], pos[1] + 1)] = EMPTY
                maze[get_list_pos(pos[0], pos[1] + 2)] = EMPTY
                pos[1] += 2
        print(*maze)


fill_map()
break_walls()

print(*maze)
