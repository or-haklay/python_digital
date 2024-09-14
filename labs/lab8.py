from random import randint

while True:
    print('''
Menu:
-----------
 1. printing 100 numbers
2. check fibo
3. randint numbers untill we get 12 or we count 10 times

0. Break
    
    ''')
    choose=input("Your choose: ")

    if choose=="1":
        for i in range(100):
            print(i)

    elif choose=="2":
        fibo = [9, 2, 11, 13, 24, 13, 21]

        boolean = "True"

        for i in range(2, len(fibo)):
            print(fibo[i])
            print(fibo[i - 1])
            print(fibo[i - 2])
            print("\n")
            if fibo[i] != (fibo[i - 1] + fibo[i - 2]):
                boolean = "Fulse"
                break

        if boolean == "True":
            print("good")
        else:
            print("bad")
    elif choose=="3":
        num=0
        counter=0
        while num!=12:
            num=randint(1,20)
            print(num)
            counter+=1
            if (num==12)or(counter==10):
                break
    elif choose=="0":
        break