"""
Mikko Sio
A01331396
"""


import time


def make_board(rows, columns):
    board = {}
    for row in range(rows):
        for column in range(columns):
            board[row, column] = "|   |"
    board[2, 2] = "| x |"
    board[4, 4] = "|Gym|"
    pokeballs = [(4, 0), (0, 2), (4, 2)]
    grass_patch = [(0, 0), (0, 1), (1, 0), (1, 1)]
    water = [(0, 4), (1, 4)]
    for coordinate in board.keys():
        if coordinate in grass_patch:
            board[coordinate] = "|, ,|"
        if coordinate in pokeballs:
            board[coordinate] = "| o |"
        if coordinate in water:
            board[coordinate] = "|~ ~|"
    board[0, 0] = "|,x,|"
    return board


def display_board(board):
    for coordinate, value in board.items():
        if coordinate[1] == 0:
            print(value, end="")
    print("")
    for coordinate, value in board.items():
        if coordinate[1] == 1:
            print(value, end="")
    print("")
    for coordinate, value in board.items():
        if coordinate[1] == 2:
            print(value, end="")
    print("")
    for coordinate, value in board.items():
        if coordinate[1] == 3:
            print(value, end="")
    print("")
    for coordinate, value in board.items():
        if coordinate[1] == 4:
            print(value, end="")
    print("")
display_board(make_board(5, 5))

def welcome_user():
    print("Hi there new trainer. My name is Professor Oak.")
    time.sleep(1)
    return input("What is your name?: ")


def make_trainer(name):
    starters = ["Charmander", "Bulbasaur", "Squirtle"]
    choices = ["1", "2", "3"]
    choice = None
    print(f"Welcome to my lab, {name}. I see that you've come for your starter Pokemon.")
    time.sleep(1)
    print("You may pick any of these three Pokemons.")
    time.sleep(1)
    for sequence_number, pokemon in enumerate(starters, 1):
        print(f"{sequence_number}: {pokemon}")
    while True:
        while choice not in choices:
            choice = input("Pick a starter Pokemon (1-3): ")
        pokemon_choice = starters[int(choice) - 1]
        print(f"Are you sure you want {pokemon_choice}?")
        confirm = input("y / n: ")
        if confirm.lower() == "y":
            break
        choice = None
    print(f"Congratulations! You have chosen {pokemon_choice}.")
    time.sleep(1)
    print("You may now start your journey on becoming the Pokemon champion!")
    time.sleep(1)
    trainer_info = {"name": name, "pokemons": [pokemon_choice]}
    return trainer_info


def get_user_choice():
    directions = ("Up", "Down", "Left", "Right")
    choices = ["1", "2", "3", "4"]
    choice = None
    for sequence_number, direction in enumerate(directions, 1):
        print(f"{sequence_number}: {direction}")
    while choice not in choices:
        choice = input("Enter a number to move (1-4): ")
    return choice


def validate_move(board, direction):
    player_position = [coordinate for coordinate, value in board.items() if "x" in value][0]
    surrounding_spaces = {(player_position[0] - 1, player_position[1]): "3",
                          (player_position[0] + 1, player_position[1]): "4",
                          (player_position[0], player_position[1] - 1): "1",
                          (player_position[0], player_position[1] + 1): "2"}
    valid_choices = []
    for coordinate, value in surrounding_spaces.items():
        if coordinate in board.keys():
            valid_choices.append(value)
    if direction in valid_choices:
        return True
    else:
        print("Not a valid move! Pick again.")
        time.sleep(1)
        return False


def move_trainer(board, direction):
    pass


def game():  # called from main
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    # name = welcome_user()
    trainer = make_trainer("Mikko")
    beat_gym = False
    while not beat_gym:
        # Tell the user where they are
        display_board(board)
        time.sleep(1)
        direction = get_user_choice()
        valid_move = validate_move(board, direction)
        if valid_move:
            move_trainer(board, direction)
            display_board(board)
            there_is_a_challenge = check_for_challenges()
            if there_is_a_challenge:
                execute_challenge_protocol(trainer)
                if trainer_has_leveled():
                    execute_glow_up_protocol()
            achieved_goal = check_if_goal_attained(board, trainer)
        else:
            pass


def main():
    game()


if __name__ == '__main__':
    main()
