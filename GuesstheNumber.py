secret_number = 6
for attempt in range(1, 4):
    guess = int(input("Enter Your Guess (1-10): "))

    if guess == secret_number:
        print("Correct! You Guessed it in", attempt, "attempt(s).")
        break
    elif guess < secret_number:
        print("Too Low! Try Again")
    else:
        print("Too High! Try Again")
else:
        print("Sorry, you Failed To Guess The Number !!")
        print("Chal! chal! chal!")