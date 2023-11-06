# Abbas Salim
# 2026396
# Initialize the roster with five players
roster = {}
for i in range(5):
    jersey = int(input(f"Enter player {i + 1}'s jersey number:\n"))
    rating = int(input(f"Enter player {i + 1}'s rating:\n\n"))
    roster[jersey] = rating

# Sort the roster by jersey number
sorted_roster = dict(sorted(roster.items()))

# Function to print the roster
def print_roster(roster):
    print("ROSTER")
    for jersey, rating in roster.items():
        print(f"Jersey number: {jersey}, Rating: {rating}")

print_roster(sorted_roster)

# Menu of options
menu = """
MENU
a - Add player
d - Remove player
u - Update player rating
r - Output players above a rating
o - Output roster
q - Quit
"""

# Loop for menu options
while True:
    print(menu)
    choice = input("Choose an option:\n")

    if choice == 'o':
        print_roster(sorted_roster)
    elif choice == 'a':
        jersey = int(input("Enter a new player's jersey number:\n"))
        rating = int(input("Enter the player's rating:\n"))
        roster[jersey] = rating
        sorted_roster = dict(sorted(roster.items()))
    elif choice == 'd':
        jersey = int(input("Enter a jersey number:\n"))
        if jersey in roster:
            del roster[jersey]
            sorted_roster = dict(sorted(roster.items()))
    elif choice == 'u':
        jersey = int(input("Enter a jersey number:\n"))
        if jersey in roster:
            rating = int(input("Enter a new rating for player:\n"))
            roster[jersey] = rating
    elif choice == 'r':
        rating = int(input("Enter a rating:\n"))
        print(f"ABOVE {rating}")
        for jersey, r in roster.items():
            if r > rating:
                print(f"Jersey number: {jersey}, Rating: {r}")
    elif choice == 'q':
        break
