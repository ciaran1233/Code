#--------
#subprograms
#-----------
#subroutine to say hello world
def hello() :
    print("hello world")

#fuction to return a string of xs
def numberofxs (number,character):
    output=""
    for i in range (number):
        output= output + character
    return output
 #-----------------------------
#main program
#----------------
hello ()
xs = int(input("enter the number of as you would like"))
print(numberofxs(xs,"x"))
print(i)
