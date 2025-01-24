'''
Objective: Create a Python program that simulates a 3x3 sliding puzzle (8-puzzle).
The puzzle consists of 8 numbered tiles and one empty space.
The goal is to arrange the tiles in ascending order from 1 to 8, with the empty space in the bottom-right corner.
'''

# solved puzzle
solved = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, '#'],
]

# test puzzle
puzzle = [
    [8, 4, '#'],
    [2, 5, 6],
    [7, 1, 3],
]

def show_puzzle():
    for row in puzzle:
        print(row)
        print('---------')


def find_tile(target):
    height = 0
    length = 0

    if target in puzzle[0]: height = 0
    if target in puzzle[1]: height = 1
    if target in puzzle[2]: height = 2

    for tile in puzzle[height]:
        if tile == target:
            break
        else:
            length += 1

    return [height, length]


def swap_tiles(empty_tile, target_tile):
    # boundary check for user_move
    for i in target_tile:
        if i not in [0, 1, 2]:
            print('Illegal move')
            return False

    # swap '#' and selected tile
    swap_value = puzzle[target_tile[0]][target_tile[1]]

    puzzle[empty_tile[0]][empty_tile[1]] = swap_value
    puzzle[target_tile[0]][target_tile[1]] = '#'

    return True


def move_tile():
    empty_tile = find_tile('#')

    while True: # validate user input move
        print('Which tile do you want to place on the EMPTY tile')
        user_move = input('L|R|U|D: ')

        if user_move.lower() in {'l', 'r', 'u', 'd'}:
            break

        print(f'{user_move} is not a legal move.')


    # get tile coordinates of user_move
    match user_move:
        # deffo bugged
        case 'L': coord = [empty_tile[0], empty_tile[1] - 1]
        case 'R': coord = [empty_tile[0], empty_tile[1] + 1]
        case 'U': coord = [empty_tile[0] - 1, empty_tile[1]]
        case 'D': coord = [empty_tile[0] + 1, empty_tile[1]]

    # debug
    print(f'coord = {coord}')
    print(f'empty_tile = {empty_tile}')

    if not swap_tiles(empty_tile, coord):
        # recursion until move is legal
        move_tile()

    return

#show_puzzle()
#move_tile()
#show_puzzle()

def main():
    moves = 0
    # game loop
    while puzzle is not solved:
        show_puzzle()
        move_tile()
        moves += 1

    print(f"Good job! You solved the puzzle in {moves} moves.")


if __name__ == '__main__':
    main()