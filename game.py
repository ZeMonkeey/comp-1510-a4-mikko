"""
Mikko Sio
A01331396
"""


def make_board(rows, columns):
    board = {}
    for row in range(rows):
        for column in range(columns):
            board[row, column] = "empty"
    board[2, 2] = "player"
    board[4, 4] = "Brock"
    pokeballs = [(4, 0), (0, 2), (4, 2)]
    grass_patch = [(0, 0), (0, 1), (1, 0), (1, 1)]
    water = [(0, 4), (1, 4)]
    for coordinate in board.keys():
        if coordinate in grass_patch:
            board[coordinate] = "grass"
        if coordinate in pokeballs:
            board[coordinate] = "pokeball"
        if coordinate in water:
            board[coordinate] = "water"
    return board


def game():  # called from main
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_trainer("Player name")
    beat_gym = False
    while not beat_gym:
        # Tell the user where they are
        current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character)
            describe_current_location(board, character)
            there_is_a_challenge = check_for_challenges()
            if there_is_a_challenge:
                execute_challenge_protocol(character)
                if character_has_leveled():
                    execute_glow_up_protocol()
            achieved_goal = check_if_goal_attained(board, character)
        else:
            pass


def main():
    pass


if __name__ == '__main__':
    main()
