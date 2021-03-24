secret_number= 7
guesses=3
while guesses<=3:
    guess = int(input("enter a guess"))
    if guess==secret_number:
        print("Congratulations, you have won!!!")
        break
    else:
        print("You have failed!")
if guesses==0:
    break
