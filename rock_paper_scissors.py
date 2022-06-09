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
        1 for Rock
        2 for paper
        3 for scissor
        """)

    user_choice = int(input("User turn: "))

    while user_choice > 3 or user_choice < 1:
        user_choice = int(input("Enter a valid input: "))

    if user_choice == 1:
        choice_name = "Rock"
    elif user_choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissor"

    print("User choice is:", choice_name)

    print("Computer turn")
    comp_choice = random.randint(1, 3)

    while comp_choice == user_choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissor"

    print("Computer choice is:", comp_choice_name)
    print(choice_name, "vs", comp_choice_name)

    if ((user_choice == 1 and comp_choice == 2) or
            (user_choice == 2 and comp_choice == 1)):
        print("Paper wins")
        result = "Paper"

    elif ((user_choice == 1 and comp_choice == 3) or
          (user_choice == 3 and comp_choice == 1)):
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
