"""
Mikko Sio
A01331396
"""


import time
import random
import pokemon_class


def make_board(rows: int, columns: int) -> dict:
    board = {}
    for row in range(rows):
        for column in range(columns):
            board[row, column] = "|   |"
    board[2, 2] = "| x |"
    board[4, 4] = "|Gym|"
    grass_patch = [(0, 0), (0, 1), (1, 0), (1, 1)]
    water = [(0, 4), (1, 4)]
    for coordinate in board.keys():
        if coordinate in grass_patch:
            board[coordinate] = "|, ,|"
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
    time.sleep(0.5)


def welcome_user():
    print("Hi there new trainer. My name is Professor Oak.")
    time.sleep(1)
    return input("What is your name?: ")


def make_starter(pokemon_choice):
    if pokemon_choice == "Charmander":
        return pokemon_class.Pokemon(pokemon_choice, "Fire", 5, ["Tackle", "Ember"])
    elif pokemon_choice == "Bulbasaur":
        return pokemon_class.Pokemon(pokemon_choice, "Grass", 5, ["Tackle", "Vine Whip"])
    elif pokemon_choice == "Squirtle":
        return pokemon_class.Pokemon(pokemon_choice, "Water", 5, ["Tackle", "Water Gun"])


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
    pokemon_choice = make_starter(pokemon_choice)
    time.sleep(1)
    print("You may now start your journey on becoming the Pokemon champion!")
    time.sleep(1)
    trainer_info = {"name": name, "pokemon": pokemon_choice,
                    "potions": 5}
    return trainer_info


def get_user_choice(board) -> tuple:
    trainer_position = [coordinate for coordinate, value in board.items() if "x" in value][0]
    directions = ("Up", "Down", "Left", "Right")
    choices = ["1", "2", "3", "4"]
    choice = None
    print("\n")
    for sequence_number, direction in enumerate(directions, 1):
        print(f"{sequence_number}: {direction}")
    while choice not in choices:
        choice = input("Enter a number to move (1-4): ")
    print("")
    if choice == "1":
        return trainer_position[0], trainer_position[1] - 1
    elif choice == "2":
        return trainer_position[0], trainer_position[1] + 1
    elif choice == "3":
        return trainer_position[0] - 1, trainer_position[1]
    elif choice == "4":
        return trainer_position[0] + 1, trainer_position[1]


def validate_move(board: dict, direction: tuple) -> bool or str:
    if direction == (4, 4):
        return "gym"

    trainer_position = [coordinate for coordinate, value in board.items() if "x" in value][0]
    surrounding_spaces = ((trainer_position[0] - 1, trainer_position[1]),
                          (trainer_position[0] + 1, trainer_position[1]),
                          (trainer_position[0], trainer_position[1] - 1),
                          (trainer_position[0], trainer_position[1] + 1))
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


def fight_gym(trainer):
    onix = pokemon_class.Pokemon("Charmander", "Rock", 10, ["Tackle", "Rock Throw"], 90)
    steelix = pokemon_class.Pokemon("Charmander", "Steel", 10, ["Iron Tail", "Rock Throw", "Dragon Breath",
                                                                "Earthquake"], 110)

    print("There is a Gym!")
    time.sleep(0.5)
    print("It is owned by the Rock-Type Gym Leader, Brock.")
    time.sleep(0.5)
    print("Would you like to challenge the Gym Leader?")
    confirm = input("y / n: ")
    if confirm.lower() == "y":
        print("So you challenge me to a Pokemon battle.")
        time.sleep(0.5)
        print("My name's Brock and I'm a Gym Leader.")
        time.sleep(0.5)
        print("When it comes to rock-hard willpower, nobody can beat me!")
        trainer["pokemon"].initiate_battle(onix, "Brock")
        trainer["pokemon"].initiate_battle(steelix, "Brock")


def check_for_events(board):
    trainer_position = [coordinate for coordinate, value in board.items() if "x" in value][0]
    if "," in board[trainer_position]:
        return "grass"
    elif "~" in board[trainer_position]:
        return "water"


def get_grass_pokemon(trainer: dict) -> object:
    level = random.randint(trainer["pokemon"].level - 3, trainer["pokemon"].level + 1)
    charmander = pokemon_class.Pokemon("Charmander", "Fire", level, ["Tackle", "Ember"])
    bulbasaur = pokemon_class.Pokemon("Bulbasaur", "Grass", level, ["Tackle", "Vine Whip"])
    charmeleon = pokemon_class.Pokemon("Charmeleon", "Fire", level, ["Tackle", "Ember", "Dragon Breath"])
    ivysaur = pokemon_class.Pokemon("Ivysaur", "Grass", level, ["Tackle", "Vine Whip", "Razor Leaf"])

    if trainer["pokemon"].level < 7:
        pokemons = [charmander, bulbasaur]
        return pokemons[random.randint(0, 1)]
    else:
        pokemons = [charmander, bulbasaur, charmeleon, charmeleon, ivysaur, ivysaur]
        return pokemons[random.randint(0, 5)]


def get_water_pokemon(trainer: dict) -> object:
    level = random.randint(trainer["pokemon"].level - 3, trainer["pokemon"].level + 1)
    squirtle = pokemon_class.Pokemon("Squirtle", "Water", level, ["Tackle", "Water Gun"])
    wartortle = pokemon_class.Pokemon("Wartortle", "Water", level, ["Tackle", "Water Gun", "Bite"])

    if trainer["pokemon"].level < 7:
        return squirtle
    else:
        pokemons = [squirtle, wartortle, wartortle]
        return pokemons[random.randint(0, 2)]


def game():  # called from main
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    # name = welcome_user()
    trainer = make_trainer("Mikko")
    beat_gym = False
    # Tell the user where they are
    display_board(board)
    while not beat_gym:
        direction = get_user_choice(board)
        valid_move = validate_move(board, direction)
        if valid_move == "gym":
            fight_gym(trainer)
            display_board(board)
        elif valid_move:
            move_trainer(board, direction)
            event_type = check_for_events(board)
            if event_type == "grass":
                wild_pokemon = get_grass_pokemon(trainer)
                print(f"A wild {wild_pokemon.name} appeared!")
                time.sleep(0.5)
                trainer["pokemon"].initiate_battle(wild_pokemon, "wild")
            elif event_type == "water":
                wild_pokemon = get_water_pokemon(trainer)
                print(f"A wild {wild_pokemon.name} appeared!")
                time.sleep(0.5)
                trainer["pokemon"].initiate_battle(wild_pokemon, "wild")
            display_board(board)
            # achieved_goal = check_if_goal_attained(board, trainer)
        else:
            print("That's not a valid move! Please pick again")
            time.sleep(1)


def main():
    game()


if __name__ == '__main__':
    main()
