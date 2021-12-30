print("Welcome to the most Awesome Game!")
name = input("What's your name? ")
age = int(input("How old are you? "))
health_points = 10

if age <= 20:
    print("Sorry, you are not eligible to play the game")
    exit()
else:
    print("First contestant's name is ", name, "and they are", age, "years old!")

def game_intro():
    print("You have", health_points)

    wants_to_play = input("Are you ready to play? ")
    if wants_to_play == "Yes":
        print("Let's start our 1st round!")
        game_round1()
    else:
        print("No problem, maybe we can play next time!")
        exit()


def game_round1():
    decision = input("Please select left or right!")
    if decision == "Left":
        health_points -= 2
        print("Oh no,", name, "you lost")
    if decision == "Right":
        health_points += 2
        print("You found gold! Now you have", health_points, "health points!")

game_intro()

def test():
    print(health_points)