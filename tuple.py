#thistuple = ("apple","banana","cherry","kiwi","orange","melon","mango")
#print(thistuple [-4:-1])
#if "apple" in thistuple:
  #  print ("yes,apple is in this tuple")
  
fruits =("apple","banana","cherry")
list_fruits = list(fruits) #creates a list from the tuple 
print(list_fruits)
list_fruits [1] = "kiwi"
print(list_fruits)
fruits =tuple(list_fruits)  #converts it into a tuple using the list
print(fruits)

  
    