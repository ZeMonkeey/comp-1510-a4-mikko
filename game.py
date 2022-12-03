"""
Mikko Sio
A01331396
"""


import time
import random


def make_board(rows: int, columns: int) -> dict:
    board = {}
    for row in range(rows):
        for column in range(columns):
            board[row, column] = "|   |"
    board[2, 2] = "| x |"
    board[4, 4] = "|Gym|"
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


def make_trainer(name: str, pokemons: dict) -> dict:
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
    trainer_info = {"name": name, "pokemons": [pokemons[pokemon_choice]],
                    "inventory": {"pokeball": 5, "potion": 5, "revive": 0}}
    return trainer_info


def get_user_choice(trainer, board) -> tuple:
    trainer_position = [coordinate for coordinate, value in board.items() if "x" in value][0]
    directions = ("Up", "Down", "Left", "Right")
    choices = ["1", "2", "3", "4"]
    choice = None
    for sequence_number, direction in enumerate(directions, 1):
        print(f"{sequence_number}: {direction}")
    while choice not in choices:
        choice = input("Enter a number to move (1-4): ")
    if choice == "1":
        return trainer_position[0], trainer_position[1] - 1
    elif choice == "2":
        return trainer_position[0], trainer_position[1] + 1
    elif choice == "3":
        return trainer_position[0] - 1, trainer_position[1]
    elif choice == "4":
        return trainer_position[0] + 1, trainer_position[1]


def validate_move(board: dict, direction: tuple) -> bool or str:
    if direction == board[(4, 0)] or direction == board[(0, 2)]:
        return "pokeball"
    elif direction == board[(4, 4)]:
        return "gym"

    trainer_position = [coordinate for coordinate, value in board.items() if "x" in value][0]
    surrounding_spaces = ((trainer_position[0] - 1, trainer_position[1]),
                          (trainer_position[0] + 1, trainer_position[1]),
                          (trainer_position[0], trainer_position[1] - 1),
                          (trainer_position[0], trainer_position[1] + 1))
    events = ("| p |", "| S |", "| H |", "|Gym|")
    valid_choices = [coordinate for coordinate in surrounding_spaces if coordinate in board.keys()]
    if direction in valid_choices:
        return True
    return False


def move_trainer(board, direction):
    trainer_position = [coordinate for coordinate, value in board.items() if "x" in value][0]
    board[trainer_position] = board[trainer_position].replace("x", " ")
    display_of_space = list(board[direction])
    display_of_space[2] = "x"
    display_of_space = "".join(display_of_space)
    board[direction] = display_of_space
    return board


def get_pokeball(trainer):
    possible_items = ("potion", "potion", "pokeball", "pokeball", "pokeball", "revive")
    print("There is a pokeball there!")
    print("You pick up the pokeball and open it.")
    reward = possible_items[random.randint(0, 5)]
    for item, value in trainer["inventory"]:
        if reward == item:
            value += 1
    return trainer


def fight_gym(trainer):
    pass


def check_for_events(board):
    trainer_position = [coordinate for coordinate, value in board.items() if "x" in value][0]
    if "," in board[trainer_position]:
        return "grass"
    elif "~" in board[trainer_position]:
        return "water"


def get_grass_pokemon(trainer: dict) -> str:
    trainer_levels = [pokemon["level"] for pokemon in trainer["pokemons"]]

    for level in trainer_levels:
        if level < 7:
            pokemons = ["Charmander", "Bulbasaur"]
            return pokemons[random.randint(0, 1)]
        else:
            pokemons = ["Charmander", "Bulbasaur", "Charmeleon", "Charmeleon", "Ivysaur", "Ivysaur"]
            return pokemons[random.randint(0, 5)]


def get_water_pokemon(trainer: dict) -> str:
    pass


def game():  # called from main
    moves = {"Tackle": 5,
             "Scratch": 5,
             "Ember": 5,
             "Flamethrower": 12,
             "Water Gun": 5,
             "Bite": 7,
             "Vine Whip": 5,
             "Razor Leaf": 6,
             "Solar Beam": 14}
    pokemons = {"Charmander": {"HP": 39, "level": 5, "moves": {"Tackle": 5, "Ember": 5}},
                "Squirtle": {"HP": 44, "level": 5, "moves": {"Tackle": 5, "Water Gun": 5}},
                "Bulbasaur": {"HP": 45, "level": 5, "moves": {"Tackle": 5, "Vine Whip": 5}},
                "Charmeleon": {"HP": 58, "level": 7, "moves": {"Tackle": 5, "Ember": 5, "Flamethrower": 12}},
                "Wartortle": {"HP": 59, "level": 7, "moves": {"Tackle": 5, "Water Gun": 5, "Bite": 7}},
                "Ivysaur": {"HP": 60, "level": 7, "moves": {"Tackle": 5, "Vine Whip": 5, "Razor Leaf": 6}},
                }
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    # name = welcome_user()
    trainer = make_trainer("Mikko", pokemons)
    beat_gym = False
    # Tell the user where they are
    display_board(board)
    time.sleep(1)
    while not beat_gym:
        direction = get_user_choice(trainer, board)
        valid_move = validate_move(board, direction)
        if valid_move == "pokeball":
            get_pokeball(trainer)
        elif valid_move == "gym":
            fight_gym(trainer)
        elif valid_move:
            move_trainer(board, direction)
            display_board(board)
            event_type = check_for_events(board)
            if event_type == "grass":
                wild_pokemon = get_grass_pokemon(trainer)
                initiate_pokemon_battle()
            elif event_type == "water":
                wild_pokemon = get_water_pokemon(trainer)
                initiate_pokemon_battle()
                # if trainer_has_leveled():
                #     execute_glow_up_protocol()
            # achieved_goal = check_if_goal_attained(board, trainer)
        else:
            print("That's not a valid move! Please pick again")
            time.sleep(1)


def main():
    game()


if __name__ == '__main__':
    main()
