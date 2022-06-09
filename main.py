import random

print("""
Winning Rules of the Rock paper scissor game as follows:
    Rock vs Paper -> Paper wins 
    Rock vs Scissor -> Rock wins 
    Paper vs Scissor -> Scissor wins
""")

while True:
    print("""
    Enter choice:
        R for Rock
        P for Paper
        S for Scissor
        """)

    user_choice = input("User turn: ").upper()

    while user_choice not in ["R", "P", "S"]:
        user_choice = input("Enter a valid input: ").upper()

    if user_choice == "R":
        choice_name = "Rock"
    elif user_choice == "P":
        choice_name = "Paper"
    else:
        choice_name = "Scissor"

    print("User choice is:", choice_name)

    print("Computer turn")
    comp_choice = random.choice(["R", "P", "S"])

    while comp_choice == user_choice:
        comp_choice = random.choice(["R", "P", "S"])

    if comp_choice == "R":
        comp_choice_name = "Rock"
    elif comp_choice == "P":
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissor"

    print("Computer choice is:", comp_choice_name)
    print(choice_name, "vs", comp_choice_name)

    if ((user_choice == "R" and comp_choice == "P") or
            (user_choice == "P" and comp_choice == "R")):
        print("Paper wins")
        result = "Paper"

    elif ((user_choice == "R" and comp_choice == "S") or
          (user_choice == "S" and comp_choice == "R")):
        print("Rock wins")
        result = "Rock"
    else:
        print("Scissor wins")
        result = "Scissor"

    if result == choice_name:
        print("User wins.")
    else:
        print("Computer wins.")

    ans = input("Do you want to play again ? (y/n)")

    if ans.upper() == "N":
        print("Goodbye.")
        break
