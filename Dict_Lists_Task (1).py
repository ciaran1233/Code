"""Complete the following tasks"""


# =========================================
# =========================================
# LISTS
# =========================================

# 1. create a list with the following items in it:
#   apple
#   banana
#   cherry
#   orange
#   cranberry
#   mango

# and print() this list
# ---


# ---

# 2. print out the length of this list
# ---


# ---

# 3. print out only the third item on the list (the "cherry")
# ---

# ---

# 4. print out the 2nd through 4th items on the list (the banana, cherry, and orange)
# ---


# ---
# 5. print out only the first 3 items on the list (apple banana cherry)
# ---


# ---


# 6. add a 'grape' to the list with append
# ---


# ---

# 7. create a second list with the following items
#   kiwi
#   melon
# and ADD this second list to your first list (saving it back into your first list)
# ---


# ---

# 8. pop the last item from the list and assign it to a new variable called 
#    "favFood"
# ---

# ---

# 9. pop the first item from the list and assign it to a new variable called
#   "hatedFood"
# ---

# ---

#10. sort the list
# ---


# ---

#11. check if "cherry" is in the list
#   if yes, then print "We have cherries!"
#   else, print "There are no cherries!"
# ---


# ---

#12. run a for loop over the entire list
#   for each loop, print out that "I love " plus the exact fruit
# ---

# ---

#13. Finally, create a for loop.  This time
#    use the range() command to tell the 'for' to loop 4 times.
#    each time print out the fruit on the list that corresponds 
#    to the INDEX number provided by the range command in the loop
# ---



# ---
# =========================================
# =========================================
# Dictionaries
# =========================================

# 14. create a dictionary with the following keys and values:
# key = 'first name', value = 'Joe'
# key = 'last name', value = 'Smith'
# key = 'id', value = 77351491
# key = 'mobile', value = '07309555055'
# key = 'email', value = 'joe.smith@email.com'
# ---


# ---

# 15. print out a list of all the keys in the dictionary
# ---



# ---

# 16. print out a list of all the values in the dictionary
# ---


# ---

# 17. print out the value of the id
# ---


# ---
# 18. change the first name value to 'susan'
# ---


# ---


# 19. get the value of the email, replace 'joe' with 'susan', and
# assign it back into the email of the dictionary
# special rules:
#   you cannot just assign "susan.smith@email.com" directly into the dictionary
#   you must
#       1) get the value,
#       2) replace joe with susan (use slicing, split(), or replace())
#       3) assign the completed value back in
# ---

person_info = {
    'first name': 'Joe',
    'last name': 'Smith',
    'id': 77351491,
    'mobile': '07309555055',
    'email': 'joe.smith@email.com'
}

# Get the current email address from the dictionary
current_email = person_info['email']

# Replace 'joe' with 'susan' in the email address
modified_email = current_email.replace('joe', 'susan')

# Assign the modified email address back to the dictionary
person_info['email'] = modified_email

# Print the updated dictionary
print(person_info)

# ---

# 20. remove the 'mobile' key/value from the dictionary
# ---


# ---
