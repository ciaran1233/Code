counter = 10   #global variable 
def increment_counter ():
    counter = 5          #llobal counter
print(counter)

increment_counter () #run function
print(counter) #prints our global function

def modify_program ():
    global counter
    counter += 1
    print(f"this is a global variable {counter}")
modify_program()
 