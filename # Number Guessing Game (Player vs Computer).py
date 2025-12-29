import random
def guess_number(x=10):
    random_number_p = random.randint(1,x)
    print("Let's play the game of finding the number that was thought!")
    attempts_p = 0
    print(f"I thought one number from 1 to {x}. Can you find?")
    while True:
        guessed_number_p = int(input(">>>"))
        attempts_p +=1
        if guessed_number_p < random_number_p :
            print("Incorrect,my thought number is greater than this one.Try once again.")
        elif guessed_number_p > random_number_p :
            print("Incorrect,my thought number is less than this one.Try once again.")
        else : 
            break
    print(f"Absolutely right, my thought number was {random_number_p}.You have found it with {attempts_p} attempts.Congratulations!\n")
    return attempts_p

def guess_number_pc(x=10):
    guessed_number_pc = 0
    print(f"Think one number from 1 to {x}.I will try to guess it.")
    input("Whenever you are ready enter anything.\n>>>")
    a = 1
    b = x
    attempts_pc = 0
    while True:
        attempts_pc += 1
        if a != b:
            guessed_number_pc = random.randint(a,b)
        else :
            guessed_number_pc = a
        check = input(f"The number that you have guessed is "
                     f"{guessed_number_pc}.Right (R),Greater than this one (G),Less than this one (L)\n>>>".lower())
        if check == 'l':
            b = guessed_number_pc - 1
        elif check == 'g':
            a = guessed_number_pc + 1
        else:
            break
    print(f"I have found your number with {attempts_pc} attempts.")
    return attempts_pc
def play(x=10):
    one_again = True
    while one_again:
        attempts_p = guess_number(x)
        attempts_pc = guess_number_pc(x)
        if attempts_p > attempts_pc :
            print("I won this game")
        elif attempts_p < attempts_pc:
            print("You won this game")
        else :
            print("TIE")
        one_again = input("Do you wanna play once again? yes(1)/no(0)\n>>>")
play()
            
            
    