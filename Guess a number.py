secret_number = 7
guess_count = 0
guess_limit = 3
while (guess_count < guess_limit):
    guess_number = int(input("Make you Guessing number:"))
    guess_count += 1
    if (guess_number == 7):
        print("You Won!")
        break
else:
    print("Sorry, you lost!")


