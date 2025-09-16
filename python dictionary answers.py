# Task 1: Create a Dictionary
# Create a dictionary with the following key-value pairs:
# 'name': 'John', 'age': 30, 'city': 'New York'
# Print the dictionary.
dictionary={
    "name" : "john",
    "age"  : "30",                                   #main variables is called dictionary,the comas are used to keep the value separate
    "city" : "new york"
}

print (dictionary)


# Task 2: Access Dictionary Values
# Access and print the value associated with the key 'age' from the dictionary created in Task 1.
# ---

dictionary = {
    "name" : "john",
    "age"  : "30",
    "city" : "new york"                 # x is the variable that represnets 30 in this.
                                        # it will now print the variable as x
}
x = dictionary ["age"]
print(x)



# Task 3: Add New Key-Value Pair
# Add a new key-value pair 'occupation': 'Engineer' to the dictionary.
# Print the updated dictionary.
# ---
dictionary ={
    "name" : "john",
    "age"  : "30",               #the brackets are used as a new value has been put into the dictionary
    "city" : "new york"
}
dictionary["occupation"]:["engineer"]

print(dictionary)

# Task 4: Update a Value
# Update the value associated with the key 'city' to 'San Francisco'.
# Print the updated dictionary.
# ---

dictionary = {
    "name" : "john",
    "age"  : "30",                       #update is used to change the city from new york to san francisco
    "city" : "new york" 
}

dictionary.update(("city" : "san francisco "))  

print(dictionary)

# Task 5: Delete a Key-Value Pair
# Delete the key-value pair with the key 'age' from the dictionary.
# Print the dictionary.
# ---

dictionary = {
    "name" : "john",
    "age"  : "30",              #.pop is used to remove age from the dictionary 
    "city" : "new york"         #
}
dictionary.pop("age")
print(dictionary)


# Task 6: Check if Key Exists
# Check if the key 'name' exists in the dictionary. Print 'Key exists' if it does, otherwise print 'Key does not exist'.
# ---

dictionary = {
    "name" : "john",
    "age"  : "30",
    "city" : "new york"
}
if "name" in dictionary                      #the if/else statement is used to define if the key exists or not and what to do if it does
    print ("key exists")                         #this is used for it to be followed if its true.
else: 
    print ("key does not exist")
print(dictionary)
# Task 7: Iterate Over Keys
# Iterate over the keys of the dictionary and print each key.
# ---
dictionary = {
    "name" : "john",
    "age"  : "30",
    "city" : "new york"        #
}

for x in dictionary :
    print(x)



# Task 8: Iterate Over Values
# Iterate over the values of the dictionary and print each value.
# ---
dictionary = {
    "name" : "john",
    "age"  : "30",
    "city" : "new york"
}

for x in dictionary:
    print(dictionary(x))
   
 # Task 9: Iterate Over Key-Value Pairs
# Iterate over the dictionary items and print each key-value pair.
# ---
dictionary = {
    "name" : "john",
    "age"  : "30",
    "city" : "new york"                                      #.items is used to show a list of the pairs used with in x and y in the dictionary
}

for x,y in dicitonary.items():
    print(x,y)
    
# Task 10: Dictionary Length
# Print the number of key-value pairs in the dictionary.
# ---
dictionary = {
    "name" : "john",
    "age"  : "30",
    "city" : "new york" # this one prints the number of pairs within the dictionary and shows it as a number.
}
x=len(dictionary)
print(x)

#advanced dictionary tasks
# Task 11: Dictionary Comprehension
# Use a dictionary comprehension to create a dictionary where the keys are numbers from 1 to 5, and the values are their squares.
# Print the dictionary.
# ---
dictionary = {
    "name" : "john",
    "age"  : "30",
    "city" : "new york"
}
# Task 14: Dictionary from List of Tuples
# Convert a list of tuples [('apple', 1), ('banana', 2), ('cherry', 3)] into a dictionary.
# Print the dictionary.
# ---