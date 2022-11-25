import argparse
import random 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
                                     "Randomly set versus race settings")
    parser.add_argument("--cc", 
                        action='store_true',
                        help = "If cc speed selection is randomized")
    parser.add_argument("--teams",
                        action='store_true',
                        help = "If teams selection is randomized")
    parser.add_argument("--items",
                        action='store_true',
                        help = "If item type selection is randomized")
    parser.add_argument("--com",
                        action='store_true',
                        help = "If computer difficulty selection is randomized")
    parser.add_argument("--vehicles",
                        action='store_true',
                        help = "If computer vehicle selection is randomized")
    parser.add_argument("--courses",
                        action='store_true',
                        help = "If course selection is randomized")
    parser.add_argument("--count",
                        action='store_true',
                        help = "If race count selection is randomized")

    args = parser.parse_args()

    if args.cc:
        ccs = ["50cc", "100cc", "150cc", "Mirror", "200cc"]
        print(f"cc speed: {random.choice(ccs)}")

    if args.teams:
        teams = ["No Teams", "Team Game"]
        print(f"teams: {random.choice(teams)}")

    if args.items:
        items = ["Normal Items",
                 "Shells Only",
                 "Bananas Only",
                 "Mushrooms Only",
                 "Bob-ombs Only",
                 "No Items",
                 "No Items or Coins",
                 "Frantic Items"]
        print(f"Items: {random.choice(items)}")

    if args.com:
        com = ["Easy COM", "Normal COM", "Hard COM"]
        print(f"COM: {random.choice(com)}")

    if args.vehicles:
        vehicles = ["All Vehicles", "Karts Only", "Bikes Only"]
        print(f"COM Vehicles: {random.choice(vehicles)}")

    if args.courses:
        courses = ["Choose", "In Order", "Random"]
        print(f"Courses: {random.choice(courses)}")

    if args.count:
        race_counts = [4, 6, 8, 12, 16, 24, 32, 48]
        print(f"Race Count: {random.choice(race_counts)}")