import random

total=0
user_chances=0
price=0
try_num=0

#intro
print("Wellcome to the Casino!! \n-------------\nEvery chance cost 3$ \n\n1)if both of the cubes equal 6 you get 1000$\n2)if the cubes are equal to the other you get 100$\n3)if then diffrent but cube 2 equal 2 you get 40$\n4)if then diffrent but cube 1 equal 1 you get 20$\n-------------"
      "")
#user chances
user_money=int(input("\nPut your money her: "))
user_chances=user_money//3
user_sper=user_money%3
print("You get " + str(user_chances) + " chances\nYou got " + str(user_sper) + "$ sper")

while user_chances > 0:
    try_num=try_num+1
    cube_1=random.randint(1,6)
    cube_2=random.randint(1,6)
    if (cube_1==cube_2) and (cube_1==6):
        price=1000
    elif cube_1==cube_2:
        price=100
    elif cube_1==1:
        price=20
    elif cube_2==2:
        price=20
    else:
        price=0
    print("\nChance number " + str(try_num) + ":\n-------------\ncube 1: " + str(cube_1) + "\ncube 2: " + str(cube_2) + "\nYou get: " + str(price) + "$")
    total=total+price
    user_chances=user_chances-1

print("\nYou win " + str(total) + "$\nYour total is: " + str(total-user_money+user_sper) + "$")