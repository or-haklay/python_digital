#תרגיל חישוב סל מחירים

#welcome massege
print("\nwellcome to are store \n\n our prices: \n tomato = 3 NIS per kg\n cucamber = 2 NIS per kg \n cola = 5 NIS \n chicken = 20 NIS per kg \n")

#what you order
tomato =   3*int(input("how many tomatos do you want (kg)?\n"))
cucmber =  2*int(input("how many cucambes do you want (kg)?\n"))
cola = 5*int(input("how many colas do you want ?\n"))
chicken = 20*int( input("how many chickens do you want (kg)?\n"))




print("\nyour summery\n------------")
print("tomato: " + str(tomato))
print("cucmber: " + str(cucmber))
print("cola: " + str(cola))
print("chicken: " + str(chicken))

print("\nyour total is: " + str(int((tomato+cucmber+cola+chicken)//1)) + " NIS without tax")
print("your total is: " + str("%.1f"%(1.17*(tomato+cucmber+cola+chicken)//1)) + " NIS with tax")




