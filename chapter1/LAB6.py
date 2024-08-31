'''
Write a code that will show the menu:
Menu:
1.Insert Number and ** it by 3
2.Insert 4 IPs to a list and print it
3. Insert 4 Entries to DNS_Dictionary and print it
4. Check if a string is Polindrom

if the user won't choose 1-4, you will tell him to insert 1-4 only!
'''



num = 0
ip_list = []
DNS_dist = {}


print('''
Menu:
1.Insert Number and ** it by 3
2.Insert 4 IPs to a list and print it
3. Insert 4 Entries to DNS_Dictionary and print it
4. Check if a string is Polindrom
''')

choose=input("Select: \n")

if(choose=="1"):
    num = int(input("Enter your Number: \n"))
    print("Your result is: " + str(num**3))

elif(choose=="2"):

    ip1=input("Enter your first IP: ")
    ip2=input("Enter your second IP: ")
    ip3=input("Enter your third IP: ")
    ip4=input("Enter your last IP: ")
    ip_list.append(ip1)
    ip_list.append(ip2)
    ip_list.append(ip3)
    ip_list.append(ip4)
    print("Your IPs list is: \n" + str(ip_list))

elif(choose=="3"):

    DNS1=input("Your first DNS: ")
    site1=input("The site: ")
    DNS2=input("Your second DNS: ")
    site2=input("The site: ")
    DNS3=input("Your third DNS: ")
    site3=input("The site: ")
    DNS4=input("Your last DNS: ")
    site4=input("The site: ")

    DNS_dist.update({DNS1:site1 , DNS2:site2 , DNS3:site3 , DNS4:site4})
    print("Your DNS Dictionary is: \n" + str(DNS_dist))

elif(choose=="4"):

    p_word=input("Enter your name: ")
    n_word=p_word[::-1]
    if(p_word==n_word):
        print("Your name is Polindrom!")
    else:
        print("Your name is'nt Polindrom!")

else:
    print("Choose number between 1-4!!!")