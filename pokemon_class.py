import random
import time


def check_advantage(move, opponent_type):
    moves = {"Tackle": "Normal",
             "Scratch": "Normal",
             "Ember": "Fire",
             "Flamethrower": "Fire",
             "Water Gun": "Water",
             "Bite": "Dark",
             "Vine Whip": "Grass",
             "Razor Leaf": "Grass",
             "Solar Beam": "Grass"}
    move_type = moves[move]
    if move_type == opponent_type:
        return "It's not very effective."

    elif move_type == "Fire" and opponent_type == "Grass":
        return "It's super effective!"
    elif move_type == "Water" and opponent_type == "Fire":
        return "It's super effective!"
    elif move_type == "Grass" and opponent_type == "Water":
        return "It's super effective!"

    elif move_type == "Grass" and opponent_type == "Fire":
        return "It's not very effective."
    elif move_type == "Fire" and opponent_type == "Water":
        return "It's not very effective."
    elif move_type == "Water" and opponent_type == "Grass":
        return "It's not very effective."


def flee_battle(pokemon_level, opponent_level):
    if pokemon_level > opponent_level:
        return random.choice((True, False, True, True, True))
    elif pokemon_level == opponent_level:
        return random.choice((True, False, True))
    elif pokemon_level < opponent_level:
        return random.choice((True, False, False))


class Pokemon:
    def __init__(self, name: str, element_type: str, level: int, moves: list):
        charmander = ["Charmander", "Charmeleon"]
        bulbasaur = ["Bulbasaur", "Ivysaur"]
        squirtle = ["Squirtle", "Wartortle"]
        self.name = name
        self.type = element_type
        self.level = level
        self.moves = moves
        self.experience = 0
        if name in charmander:
            self.health = round(7.5 * level, 0)
        elif name in bulbasaur:
            self.health = round(8.5 * level, 0)
        elif name in squirtle:
            self.health = round(8 * level, 0)

    def evolve_pokemon(self):
        evolutions = ["Charmander", "Squirtle", "Bulbasaur",
                      "Charmeleon", "Wartortle", "Ivysaur",
                      "Charizard", "Blastoise", "Venasaur"]

        while self.level >= 7 and self.name not in evolutions[6:9]:
            index = evolutions.index(self.name)
            pre_evolution = self.name
            self.name = evolutions[index + 3]
            print(f"{pre_evolution} has evolved into {self.name}!")

    def level_up(self):
        experience_points = self.experience
        while experience_points > 0:
            self.experience -= 100
            if self.experience >= 0:
                self.level += 1
                self.health += 10
                experience_points -= 100
            else:
                self.experience = experience_points
                break
        self.evolve_pokemon()

    def gain_exp(self, opponent):
        level_difference = self.level - opponent.level

    def fight_wild_pokemon(self, opponent):
        escape = False
        max_health = self.health
        opponent_max_health = opponent.health
        move_powers = {"Tackle": 8,
                       "Scratch": 8,
                       "Ember": 8,
                       "Flamethrower": 16,
                       "Water Gun": 8,
                       "Bite": 10,
                       "Vine Whip": 8,
                       "Razor Leaf": 9,
                       "Solar Beam": 19}
        print(f"A wild {opponent.name} appeared!")
        time.sleep(0.5)
        print(f"You send out {self.name}!")

        while self.health > 0 and opponent.health > 0 and not escape:
            self.health = round(self.health, 2)
            opponent.health = round(opponent.health, 2)
            time.sleep(0.5)
            print(f"\n{self.name}   HP {self.health} / {max_health}")
            print(f"{opponent.name}   HP {opponent.health} / {opponent_max_health}")
            time.sleep(0.5)
            print("")
            choices = ("Fight", "Heal", "Flee")
            for number, choice in enumerate(choices, 1):
                print(f"{number}: {choice}")

            choices = ["1", "2", "3"]
            choice = None
            while choice not in choices:
                choice = input("What do you want to do?: ")
                print("")

            if choice == "1":
                for number, move in enumerate(self.moves, 1):
                    print(f"{number}: {move}")
                move = input("Pick a move: ")

                try:
                    move = self.moves[int(move) - 1]
                except IndexError:
                    print("\nThat is not a move.")
                    time.sleep(0.5)
                    continue
                except ValueError:
                    print("\nPlease pick a number.")
                    time.sleep(0.5)
                    continue

                damage = move_powers[move]
                advantage = check_advantage(move, opponent.type)

                if advantage == "It's super effective!":
                    print("\n" + advantage)
                    damage *= 2
                elif advantage == "It's not very effective.":
                    print("\n" + advantage)
                    damage /= 2

                time.sleep(0.5)
                damage = round(damage, 2)
                opponent.health -= damage
                print(f"You hit the opposing pokemon for {damage} damage!")
                time.sleep(1)

            elif choice == "2":
                if self.health < max_health:
                    self.health += 10
                    print(f"You healed {self.name}.\n")
                    if self.health > max_health:
                        self.health = max_health
                elif self.health == max_health:
                    print(f"{self.name} is already at max health.\n")

            elif choice == "3":
                escape = flee_battle(self.level, opponent.level)
                if not escape:
                    print("You failed to flee.")

            if opponent.health <= 0:
                print("The opposing pokemon has fainted!")
                break

            # opponent's turn
            opponent_attack = random.choice(opponent.moves)

            damage = move_powers[opponent_attack] / 1.5
            advantage = check_advantage(opponent_attack, self.type)
            print(f"The wild {opponent.name} uses {opponent_attack}")

            if advantage == "It's super effective!":
                print("\n" + advantage)
                damage *= 2
            elif advantage == "It's not very effective.":
                print("\n" + advantage)
                damage /= 2

            time.sleep(0.5)
            damage = round(damage, 2)
            self.health -= damage
            print(f"It deals {damage} damage.")
            time.sleep(1)

            if self.health <= 0:
                print(f"{self.name} has fainted!")
                break

        if escape:
            print("You have successfully fled.")
        self.health = max_health
        opponent.health = opponent_max_health


def main():
    charmander = Pokemon("Charmander", "Fire", 5, ["Tackle", "Ember"])
    squirtle = Pokemon("Squirtle", "Water", 5, ["Tackle", "Water Gun"])
    bulbasaur = Pokemon("Bulbasaur", "Grass", 5, ["Tackle", "Vine Whip"])
    print(charmander.health)
    print(bulbasaur.health)
    print(squirtle.health)
    charmander.level_up()
    # charmander.fight_wild_pokemon(charmander)


if __name__ == '__main__':
    main()
