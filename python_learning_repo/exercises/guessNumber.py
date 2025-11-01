import random as r

maximum=int(input("Enter the cell: "))
minimum=int(input("Enter the floor: "))
target_number=r.randint(minimum, maximum)
chance=eval(input("Enter the times you can guess: "))
while chance!=0 :
    temp=int(input("Enter what you guess: "))
    if temp>maximum or temp<minimum:
        print("Out of the range! Reinput please. What de hell are you doing?")
        continue
    elif temp==target_number:
        print("Bingo! The number is {}".format(target_number))
        break
    elif temp>target_number:
        print("Too big!")
    else:
        print("Too small!")
    chance-=1
if chance==0:
    print("Game over! You have used all your chances. The number is {}".format(target_number))

