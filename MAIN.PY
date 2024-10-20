import random

def game(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == '2':
            return False
        elif you == '3':
            return True
    elif comp == 'w':
        if you == '3':
            return False
        elif you == '1':
            return True
    elif comp == 'g':
        if you == '1':
            return False
        elif you == '2':
            return True

print("comp's turn: snake (s) water (w) gun (g)")
randno = random.randint(1, 3)

if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
else:
    comp = 'g'

print(f"comp chose: {comp}")

you = input("your turn: snake (1) water (2) gun (3): ")

result = game(comp, you)

if result is None:
    print("It's a tie!")
elif result:
    print("You win!")
else:
    print("Computer wins!")
