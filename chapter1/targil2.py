#תרגיל חישוב סל מחירים

#welcome massege
print("\nwellcome to are store \n\n our prices: \n tomato = 3 NIS per kg\n cucamber = 2 NIS per kg \n cola = 5 NIS \n chicken = 20 NIS per kg \n")

#what you order
tamato = int(input("how many tomatos do you want (kg)?\n"))
cucmber = int(input("how many cucambes do you want (kg)?\n"))
cola = int(input("how many colas do you want ?\n"))
chicken = int( input("how many chickens do you want (kg)?\n"))

print("your total is: " + str(int(1.17*(tamato+cucmber+cola+chicken)//1)) + " NIS")













