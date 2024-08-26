num=4587

Alafim=num//1000
print(Alafim)
Meot=(num-Alafim*1000)//100
print((Meot))
Asarot=(num-Alafim*1000-Meot*100)//10
print(Asarot)
Ahadot=(num-Alafim*1000-Meot*100-Asarot*10)//1
print(Ahadot)


print("Alafim= " + str(num//1000))


print("Meot= " + str((num%1000)//100))


print("Asarot= " + str((num%100)//10))


print("Ahado= " + str((num%10)//1))