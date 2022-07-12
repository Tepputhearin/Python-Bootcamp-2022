import random

intro_message = "Welcome to the dices game!"
after_roll = "=========="
num_loop_end = 1
error = "USAGE :The number must be between 1 and 8"
# function use to prepare for number of rolls of the dice
def dice_rolls(int_num):
    result = 0
    if int_num == 1:
        random_dice = random.randint(1, 6)
        print(f"RESULT:{random_dice}")
    elif int_num > 1:
        if int_num <= 8:
            for i in range(0, int_num):
                random_dice = random.randint(1, 6)  # numbers that contain 1 to 6 randomly output when call
                print(f"Dice {i+1} : {random_dice}")  # Display rolls and output of dice
                result += random_dice               # Add to value for each loop
            print(f"{after_roll}\nRESULT:{result}\n{after_roll}")
    return
# function to check if number is integer or str or other

print(intro_message)
while True:
    num_dice = input("Enter the number of dices you want to roll:")
    if num_dice.isdigit():
        int_num = int(num_dice)
        if int_num < 9:
            dice_rolls(int_num)  # if it is a number type it would go to the dice_rolls function
            break
        else:
            print(error)
    else:
        print(error)
