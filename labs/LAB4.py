my_list=["or haklay", 23, "or.haklay@gmail.com", "0558827804"]
print("full name: " + my_list[0] + "\nage: " + str(my_list[1]) + "\nmail: " + my_list[2] +"\nphone number: " + my_list[3])

ip_list=["123.123.123", "234.234.234"]
print(ip_list)
print(len(ip_list))

ip_list.append("345.345.345")
ip_list.append("456.456.456")
ip_list.append("567.567.567")
print(ip_list)
print(len(ip_list))

ip_list.pop(2)
print(ip_list)
print(len(ip_list))