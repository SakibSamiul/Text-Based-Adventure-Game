answer = input("Do you want to play this game? [Yes/No]: ")


if answer == "Yes":
    print("Welcome to the Game!")

    answer = input("Do you want to go jungle or cave? [jungle/cave]")
    if answer == "jungle":
        print("You see the hungry tiger.")
        answer = input("Do you want to fight with the tiger or run away! [fight/run]")
        if answer == "fight":
            print("Tiger will eat you. You dead.")
        else:
            print("WOW! Still you are alive!")
    elif answer == "cave":
        print("You see the bear in front of the cave")
        answer = input("Do you want to fight with the bear or run away! [fight/run]")
        if answer == "fight":
            print("bear is too much strong! You loss the game.")

        else:
            print("WOW! still you are alive!")

else:
    print("Please play this game at least one time")
