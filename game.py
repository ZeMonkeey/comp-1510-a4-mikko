"""
Mikko Sio
A01331396
"""


import time


def make_board(rows: int, columns: int) -> dict:
    board = {}
    for row in range(rows):
        for column in range(columns):
            board[row, column] = "|   |"
    board[2, 2] = "| x |"
    board[4, 4] = "|Gym|"
    board[4, 1] = "| S |"
    board[4, 2] = "| H |"
    pokeballs = [(4, 0), (0, 2)]
    grass_patch = [(0, 0), (0, 1), (1, 0), (1, 1)]
    water = [(0, 4), (1, 4)]
    for coordinate in board.keys():
        if coordinate in grass_patch:
            board[coordinate] = "|, ,|"
        if coordinate in pokeballs:
            board[coordinate] = "| p |"
        if coordinate in water:
            board[coordinate] = "|~ ~|"
    return board


def display_board(board: dict):
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


def welcome_user():
    print("Hi there new trainer. My name is Professor Oak.")
    time.sleep(1)
    return input("What is your name?: ")


def make_trainer(name: str) -> dict:
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


def get_user_choice() -> str:
    directions = ("Up", "Down", "Left", "Right")
    choices = ["1", "2", "3", "4"]
    choice = None
    for sequence_number, direction in enumerate(directions, 1):
        print(f"{sequence_number}: {direction}")
    while choice not in choices:
        choice = input("Enter a number to move (1-4): ")
    return choice


def validate_move(board: dict, direction: str) -> bool:
    trainer_position = [coordinate for coordinate, value in board.items() if "x" in value][0]
    surrounding_spaces = {(trainer_position[0] - 1, trainer_position[1]): "3",
                          (trainer_position[0] + 1, trainer_position[1]): "4",
                          (trainer_position[0], trainer_position[1] - 1): "1",
                          (trainer_position[0], trainer_position[1] + 1): "2"}
    valid_choices = []
    for coordinate, value in surrounding_spaces.items():
        if coordinate in board.keys():
            valid_choices.append(value)
    if direction in valid_choices:
        return True
    return False


def move_trainer(board, direction):
    trainer_position = [coordinate for coordinate, value in board.items() if "x" in value][0]
    board[trainer_position] = board[trainer_position].replace("x", " ")
    space_to_move_into = None
    if direction == "1":
        space_to_move_into = (trainer_position[0], trainer_position[1] - 1)
    elif direction == "2":
        space_to_move_into = (trainer_position[0], trainer_position[1] + 1)
    elif direction == "3":
        space_to_move_into = (trainer_position[0] - 1, trainer_position[1])
    elif direction == "4":
        space_to_move_into = (trainer_position[0] + 1, trainer_position[1])
    display_of_space = list(board[space_to_move_into])
    display_of_space[2] = "x"
    display_of_space = "".join(display_of_space)
    board[space_to_move_into] = display_of_space
    return board


def check_for_events(board):
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
            event_type = check_for_events(board)
            if event_type == "grass":
                execute_challenge_protocol(trainer)
            elif event_type == "water":
                pass
            elif event_type == "pokeball":
                pass

                # if trainer_has_leveled():
                #     execute_glow_up_protocol()
            # achieved_goal = check_if_goal_attained(board, trainer)
        else:
            print("Not a valid move! Pick again.")
            time.sleep(1)


def main():
    game()


if __name__ == '__main__':
    main()
