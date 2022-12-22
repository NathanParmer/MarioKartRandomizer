import argparse
import json
import random

teams = ["Red", "Blue"]

class Player:
    def __init__(self, i: int, num_players: int, controllers: dict, 
                 is_team: bool, characters: dict, bodies: dict, wheels: dict, 
                 gliders: dict):
        self.index = i
        if controllers:
            self.set_controller(i, num_players, controllers)
        else:
            self.controller = None
        self.set_team(is_team)
        self.set_character(characters)
        self.set_body(bodies)
        self.set_wheel(wheels)
        self.set_glider(gliders)

    def set_controller(self, i: int, num_players: int, controllers: dict):
        controller_idx = random.randint(0, num_players - i)
        self.controller = controllers[str(num_players)][controller_idx]
        controllers[str(num_players)].pop(controller_idx)

    def set_team(self, is_team: bool):
        self.team = None
        if is_team:
            self.team = random.choice(teams)

    def set_character(self, characters: dict):
        self.character = random.choice(list(characters.keys()))

    def set_body(self, bodies: dict):
        self.body = random.choice(list(bodies.keys()))

    def set_wheel(self, wheels: dict):
        self.wheel = random.choice(list(wheels.keys()))

    def set_glider(self, gliders: dict):
        self.glider = random.choice(list(gliders.keys()))

    def print_player(self):
        print(f"Player {self.index}:")
        if self.controller:
            print(f"  Controller: {self.controller}")
        if self.team is not None:
            print(f"  Team: {self.team}")
        print(f"  Character: {self.character}")
        print(f"  Body: {self.body}")
        print(f"  Wheels: {self.wheel}")
        print(f"  Gliders: {self.glider}")
        print("")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get random Mario Kart 8 character and\
                                     kart combinations from the command line")
    parser.add_argument("--players", default=1, type=int,
                        help="Number of players")
    parser.add_argument("--controllers", default=None, type=str, 
                        help="Path of the controller json file")
    parser.add_argument("--team", action='store_true',
                        help="If players are assigned a team")
    parser.add_argument("--characters", default="./base_game/characters.json",
                        type=str, help="Path of the character json file")
    parser.add_argument("--bodies", default="./base_game/bodies.json",
                        type=str, help="Path of the bodies json file")
    parser.add_argument("--wheels", default="./base_game/wheels.json",
                        type=str, help="Path of the wheels json file")
    parser.add_argument("--gliders", default="./base_game/gliders.json",
                        type=str, help="Path of the gliders json file")
    args = parser.parse_args()

    if args.players < 1 or args.players > 4:
        raise ValueError("Must have 1-4 players")

    if args.controllers:
        with open(args.controllers, 'r') as controller_json:
            controller_dict = json.load(controller_json)
    else:
        controller_dict = None

    def get_character_dict(character_json_path):
        with open(character_json_path, 'r') as character_json:
            character_dict = json.load(character_json)
        character_dict = {k:v for (k, v) in character_dict.items() if v["Enable"] == True}
        return character_dict
    character_dict = get_character_dict(args.characters)

    def get_body_dict(body_json_path):
        with open(body_json_path, 'r') as body_json:
            body_dict = json.load(body_json)
        body_dict = {k:v for (k, v) in body_dict.items() if v["Enable"] == True}
        return body_dict
    body_dict = get_body_dict(args.bodies)

    def get_wheels_dict(wheel_json_path):
        with open(wheel_json_path, 'r') as wheel_json:
            wheels_dict = json.load(wheel_json)
        wheels_dict = {k:v for (k, v) in wheels_dict.items() if v["Enable"] == True}
        return wheels_dict
    wheels_dict = get_wheels_dict(args.wheels)

    def get_glider_dict(glider_json_path):
        with open(glider_json_path, 'r') as glider_json:
            glider_dict = json.load(glider_json)
        glider_dict = {k:v for (k, v) in glider_dict.items() if v["Enable"] == True}
        return glider_dict
    glider_dict = get_glider_dict(args.gliders)

    for i in range(args.players):
        player_i = Player(i + 1, args.players, controller_dict, args.team, 
                          character_dict, body_dict, wheels_dict, glider_dict)
        player_i.print_player()
