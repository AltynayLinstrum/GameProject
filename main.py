print("Welcome to the most Awesome Game!")
name = input("What's your name? ").lower()
age = int(input("How old are you? "))
health_points = 10

if age <= 20:
    print("Sorry, you are not eligible to play the game")
    exit()
else:
    print("First contestant's name is ", name, "and they are", age, "years old!")

wants_to_play = input("You have 10 health points! Are you ready to play? ")
if wants_to_play == "yes":
    print("Let's start our 1st round!")
    left_or_right = input("Please choose if you'd like to turn left or right! ")
    if left_or_right == "Left":
        print("Oh no, there was a big crocodile on the left, and you lose 2 health points!")
        health_points -= 2
        print("Now you have only", health_points, "point left!")
        try_again = input("Would you like to try again?")
        if try_again == "Yes":
            try_again2 = input("Please choose if you'd like to turn left or right! ")
            if try_again2 == "Left":
                print("Oh no, there was a big crocodile on the left, and you lose 2 health points!")
                health_points -= 2
                print("Now you have only", health_points, "point left!")
            if try_again2 == "Right":
                print("Great choice! You found a pot of gold!")
                health_points += 2
                print ("Now you have,", health_points, "health points! ")


        else: 
            print("Good Bye!")

    if left_or_right == "Right":
        print("Great choice! You found a pot of gold!")
        health_points += 2
        print ("Now you have,", health_points, "health points! ")

else:
    print("No problem, maybe we can play next time!")
    exit()


