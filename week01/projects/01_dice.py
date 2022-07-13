import random

intro_message = "Welcome to the dices game!"
after_roll = "=========="
num_loop_end = 1
error = "USAGE :The number must be between 1 and 8"


def dice_rolls(int_number):                              # function use to prepare for number of rolls of the dice
    result = 0
    if int_number == 1:                                  # function to check if number is 1
        random_dice = random.randint(1, 6)               # numbers that contain 1 to 6 randomly output when call
        print(f"RESULT:{random_dice}")
    elif int_number > 1:                                 # check if number is other than 1
        if int_number <= 8:                              # check if number is from 2 to 8
            for i in range(0, int_number):
                random_dice = random.randint(1, 6)
                print(f"Dice {i+1} : {random_dice}")     # Display rolls and output of dice each loop
                result += random_dice                    # Add to value for each loop
            print(f"{after_roll}\nRESULT:{result}\n{after_roll}")
    return

# Operation starts here:


print(intro_message)
while True:                                              # It would loop the input if invalid and or not
    numbers_dice = input("Enter the number of dices you want to roll:")
    if numbers_dice.isdigit():                           # Check if something is other than a number
        int_number = int(numbers_dice)
        if int_number < 9:
            dice_rolls(int_number)                       # it would go to the dice_rolls function
            break
        else:
            print(error)
    else:
        print(error)
