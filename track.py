import argparse
import json
import random

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get a random Mario Kart 8 Deluxe track from the command line")
    parser.add_argument("--number",
                        default= -1,
                        type=int,
                        help="Number of tracks to select")
    parser.add_argument("--tracks",
                        default="./base_game/tracks.json",
                        type=str,
                        help="Path of the tracks json")
    parser.add_argument("--replace",
                        default=False,
                        type=bool,
                        help="If the track should be replaced upon selection")
    args = parser.parse_args()

    with open(args.tracks, 'r') as track_json:
        tracks = json.load(track_json)

    if (args.number == -1):
        n = len(tracks)
    else:
        n = args.number
        
    for i in range(n):
        a = input("")
        track = random.choice(list(tracks.keys()))
        cup = tracks[track]["Cup"]
        print(f"{cup} Cup: {track}")
        if not args.replace:
            tracks.pop(track)