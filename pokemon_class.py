import random
import time


def check_advantage(move, opponent_type):
    moves = {"Tackle": "Normal",
             "Dragon Breath": "Dragon",
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
        self.experience = 510
        if name in charmander:
            self.health = round(7.5 * level, 0)
        elif name in bulbasaur:
            self.health = round(8.5 * level, 0)
        elif name in squirtle:
            self.health = round(8 * level, 0)
        self.max_health = self.health

    def add_new_moves(self):
        moves = {"Charmeleon": "Dragon Breath",
                 "Charizard": "Flamethrower",
                 "Wartortle": "Bite",
                 "Blastoise": "Hydro Pump",
                 "Ivysaur": "Razor Leaf",
                 "Venasaur": "Solar Beam"}
        self.moves.append(moves[self.name])
        print(f"{self.name} has learned {moves[self.name]}!\n")
        time.sleep(0.5)

    def evolve_pokemon(self, evolutions):
        index = evolutions.index(self.name)
        pre_evolution = self.name
        self.name = evolutions[index + 3]
        print("Your pokemon is evolving!!")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1.5)
        print(f"{pre_evolution} has evolved into {self.name}!")
        time.sleep(0.5)
        self.add_new_moves()

    def level_up(self):
        evolutions = ["Charmander", "Squirtle", "Bulbasaur",
                      "Charmeleon", "Wartortle", "Ivysaur",
                      "Charizard", "Blastoise", "Venasaur"]
        experience_points = self.experience
        while experience_points > 0:
            self.experience -= 100
            if self.experience >= 0:
                self.level += 1
                self.max_health += 10
                experience_points -= 100
                time.sleep(0.5)
                print(f"{self.name} has levelled up to level {self.level}!")
            else:
                self.experience = experience_points
                break
        if 10 >= self.level >= 7 and self.name not in evolutions[3:6]:
            self.evolve_pokemon(evolutions)
        if self.level >= 10 and self.name not in evolutions[6:9]:
            self.evolve_pokemon(evolutions)

    def gain_exp(self, opponent):
        exp_gained = random.randint(70, 80)
        if self.level > opponent.level:
            exp_gained -= 5 * (self.level - opponent.level)
        elif self.level < opponent.level:
            exp_gained += 7 * (opponent.level - self.level)
        print(f"{self.name} has gained {exp_gained} xp!")
        self.experience += exp_gained
        self.level_up()

    def fight_wild_pokemon(self, opponent):
        escape = False
        move_powers = {"Tackle": 8,
                       "Dragon Breath": 10,
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

        # battle starts
        print("")
        print("----- Wild Pokemon Encounter -----")
        while self.health > 0 and opponent.health > 0 and not escape:
            # pokemon information
            self.health = round(self.health, 2)
            opponent.health = round(opponent.health, 2)
            time.sleep(0.5)
            print("")
            print("----------------------------------")
            print(f"{self.name}    Lv.{self.level}\n    |HP {self.health} / {self.max_health}|")
            print("----------------------------------")
            print("")
            print("----------------------------------")
            print(f"{opponent.name}    Lv.{opponent.level}\n    |HP {opponent.health} / {opponent.max_health}|")
            print("----------------------------------")
            time.sleep(0.5)
            print("")
            choices = ("Fight", "Heal", "Flee")

            # your turn
            for number, choice in enumerate(choices, 1):
                print(f"{number}: {choice}")

            choices = ["1", "2", "3"]
            choice = None
            while choice not in choices:
                choice = input("What do you want to do?: ")
                print("")

            # attack opponent
            if choice == "1":
                for number, move in enumerate(self.moves, 1):
                    print(f"{number}: {move}")
                move = input("Pick a move: ")
                print("")

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
                # calculate damage
                damage = move_powers[move]
                advantage = check_advantage(move, opponent.type)
                if advantage == "It's super effective!":
                    print(advantage)
                    damage *= 2
                elif advantage == "It's not very effective.":
                    print(advantage)
                    damage /= 2
                time.sleep(0.5)
                damage = round(damage, 2)
                opponent.health -= damage
                print(f"You hit the opposing pokemon for {damage} damage!")
                time.sleep(1)

            # heal pokemon
            elif choice == "2":
                if self.health < self.max_health:
                    self.health += 10
                    print(f"You healed {self.name}.\n")
                    if self.health > self.max_health:
                        self.health = self.max_health
                elif self.health == self.max_health:
                    print(f"{self.name} is already at max health.\n")

            # run away
            elif choice == "3":
                escape = flee_battle(self.level, opponent.level)
                if not escape:
                    print("You failed to flee.")

            # check if opponent is dead
            if opponent.health <= 0:
                print("The opposing pokemon has fainted!")
                self.gain_exp(opponent)
                break

            # opponent's turn
            opponent_attack = random.choice(opponent.moves)

            damage = move_powers[opponent_attack] / 1.5
            advantage = check_advantage(opponent_attack, self.type)
            print(f"\nThe wild {opponent.name} uses {opponent_attack}")
            time.sleep(0.5)

            # calculate damage
            if advantage == "It's super effective!":
                print(advantage)
                damage *= 2
            elif advantage == "It's not very effective.":
                print(advantage)
                damage /= 2
            time.sleep(0.5)
            damage = round(damage, 2)
            self.health -= damage
            print(f"It deals {damage} damage.")
            time.sleep(1)

            # check if you are dead
            if self.health <= 0:
                print(f"{self.name} has fainted!")
                break

        if escape:
            print("You have successfully fled.")
        self.health = self.max_health
        opponent.health = opponent.max_health


def main():
    charmander = Pokemon("Charmander", "Fire", 5, ["Tackle", "Ember"])
    squirtle = Pokemon("Squirtle", "Water", 5, ["Tackle", "Water Gun"])
    bulbasaur = Pokemon("Bulbasaur", "Grass", 5, ["Tackle", "Vine Whip"])
    charmander.fight_wild_pokemon(bulbasaur)
    charmander.fight_wild_pokemon(bulbasaur)
    print(charmander.experience)
    print(charmander.level)


if __name__ == '__main__':
    main()
