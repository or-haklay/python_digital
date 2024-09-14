import random
from time import sleep

total=0
user_chances=0
prize=0
try_num=0

#intro
print("Wellcome to the Casino!! \n-------------\nEvery chance cost 3$ \n\n1)if both of the cubes equal 6 you get 1000$\n2)if the cubes are equal to the other you get 100$\n3)if then diffrent but cube 2 equal 2 you get 40$\n4)if then diffrent but cube 1 equal 1 you get 20$\n-------------"
      "")
#user chances
user_money=int(input("\nPut your money here: "))
user_chances=user_money//3
user_sper=user_money%3
print("You get " + str(user_chances) + " Rollings\nYou got " + str(user_sper) + "$ sper")

for i in range (user_chances):
    try_num=try_num+1
    print("\nRolling number " + str(try_num) + ":\n-------------\n")
    sleep(2)
    cube_1=random.randint(1,6)
    cube_2=random.randint(1,6)
    if (cube_1==cube_2) and (cube_1==6):
        prize=1000
    elif cube_1==cube_2:
        prize=100
    elif cube_1==1:
        prize=20
    elif cube_2==2:
        prize=20
    else:
        prize=0
    print("cube 1: " + str(cube_1) + "\ncube 2: " + str(cube_2) + "\nYou get: " + str(prize) + "$")
    total=total+prize
    user_chances=user_chances-1

sleep(1)
print("\nYou win " + str(total) + "$")
sleep(0.5)
print("Your total is: " + str(total-user_money+user_sper) + "$")