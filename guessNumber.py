from random import randint

number = randint(0, 1)
print(f"answer is: {number}")
tries = 3
while tries > 0:
    guess = int(input("Enter number: "))
    if number == guess:
        print("You won")
        break
    else:
        tries -= 1