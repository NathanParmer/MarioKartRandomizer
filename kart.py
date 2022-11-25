import argparse
import json
import random

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 
                                     "Get random Mario Kart 8 character and\
                                     kart combinations from the command line")
    parser.add_argument("--players", default=1, type=int, 
                        help="Number of players")
    parser.add_argument("--characters", 
                        default="./base_game/characters.json", 
                        type=str,
                        help="Path of the character json file")
    parser.add_argument("--bodies", 
                        default="./base_game/bodies.json", 
                        type=str,
                        help="Path of the bodies json file")
    parser.add_argument("--wheels", 
                        default="./base_game/wheels.json", 
                        type=str,
                        help="Path of the wheels json file")
    parser.add_argument("--gliders", 
                        default="./base_game/gliders.json", 
                        type=str,
                        help="Path of the gliders json file")
    args = parser.parse_args()

    with open(args.characters, 'r') as character_json:
        characters = json.load(character_json)
    with open(args.bodies, 'r') as body_json:
        bodies = json.load(body_json)
    with open(args.wheels, 'r') as wheel_json:
        wheels = json.load(wheel_json)
    with open(args.gliders, 'r') as glider_json:
        gliders = json.load(glider_json)

    for i in range(args.players):
        character   = random.choice(list(characters.keys()))

        body_idx    = random.randint(1, len(bodies) - 1)
        body        = list(bodies.keys())[body_idx]

        wheel_idx   = random.randint(1, len(wheels) - 1)
        wheel       = list(wheels.keys())[wheel_idx]
        
        glider_idx   = random.randint(1, len(gliders) - 1)
        glider       = list(gliders.keys())[glider_idx]

        print(f"Player {i + 1}:")
        print("Character:", character)
        print(f"Body ({body_idx}): {body}")
        print(f"Wheels ({wheel_idx}): {wheel}")
        print(f"Gliders ({glider_idx}): {glider}")
        print("")