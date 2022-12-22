# Mario Kart Randomizer

As I was playing Mario Kart with my family during Thanksgiving, we realized that the racing game wasn't chaotic enough for our tastes. Having control over selecting your character/kart combination, the tracks, and game settings gave players who were good at the game an unfair advantage. Removing any and all control was the only solution.

I created this with Mario Kart 8 Deluxe and VS races in mind. If there's interest, I'm open to adding functionality for other titles or game modes in the series. I'd like to experiment with creating a GUI to make it more accessible, as well.

The characters, karts, tracks, and items are all copyrighted by Nintendo, and I do not claim ownership over their work. This is a free aid intended as a supplement to the game, and I do not profit off of it. 

## Character Selection, Kart Creation, and Team Assignment
The `kart.py` script handles character and kart creation, as well as team assignment if desired. See usage below:
```
python3 kart.py --help
```
```
usage: kart.py [-h] [--players PLAYERS] [--team] [--characters CHARACTERS] [--bodies BODIES] [--wheels WHEELS] [--gliders GLIDERS]

Get random Mario Kart 8 character and kart combinations from the command line

options:
  -h, --help                show this help message and exit
  --players PLAYERS         Number of players
  --team                    If players are assigned a team
  --characters CHARACTERS   Path of the character json file
  --bodies BODIES           Path of the bodies json file
  --wheels WHEELS           Path of the wheels json file
  --gliders GLIDERS         Path of the gliders json file
```

### The use of json files
I've provided the option to specify custom json files for different characters, bodies, wheels, and gliders. The default json files in the `base_game/` directory contain all non-DLC content for Mario Kart 8 Deluxe, but you may not have unlocked all of the customization options yet, or perhaps you have more. In that case, you can modify the json in `base_game/` with the stuff you have on your copy of the game. This is helpful if you play with both Player A and Player B and want to be able to switch between them.

JSON files are also useful, as they make it simple to add different properties to the characters or kart components.

## Track Selection
You can also select tracks at random. While Mario Kart does have a random track selection, we found it often chose tracks we had just played awhile earlier. By default, the script won't choose a track more than once, though you can disable this behavior with the `--replace` flag below. See usage below:
```
python3 track.py -h
```
```
usage: track.py [-h] [--number NUMBER] [--tracks TRACKS] [--replace]

Get a random Mario Kart 8 Deluxe track from the command line

options:
  -h, --help       show this help message and exit
  --number NUMBER  Number of tracks to select
  --tracks TRACKS  Path of the tracks json
  --replace        If the track should be replaced upon selection
```
Again, I've created an optional parameter to specify the path of a custom track json file. The one I've included doesn't have the new DLC tracks (yet), so you may want to expand on that.

## VS Race Settings
We wanted to be able to randomize factors like the speed and item types, so this script was born. Usage below:
```
python3 versus.py -h
```
```
usage: versus.py [-h] [--cc] [--teams] [--items] [--com] [--vehicles] [--courses] [--count]

Randomly set versus race settings

options:
  -h, --help  show this help message and exit
  --cc        If cc speed selection is randomized
  --teams     If teams selection is randomized
  --items     If item type selection is randomized
  --com       If computer difficulty selection is randomized
  --vehicles  If computer vehicle selection is randomized
  --courses   If course selection is randomized
  --count     If race count selection is randomized
