#create dictionary with 5 name and there money
my_dict={"or":35000 , "orian":15000 , "yuval":10000 , "shaked":20000 , "roi":30000}

#sum first and last names, print nice
sum = my_dict["or"]+my_dict["roi"]
print("Or and Roi have " + str(sum) + "$ together\n")

#add new name=dudu, his valeu equal to first and last sum
my_dict.update({"ron":65000})
print(my_dict)

#print the number of entries and check if "idan" is inside
print("\nThere are " + str(len(my_dict)) + " names in my list!")
