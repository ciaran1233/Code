retireage = 65
userage =int(input("enter your age:"))
if userage>=retireage:
    print("your're already retired!")
elif userage<0:
    print("you are not born yet!")
    
else:
    print("you have",retireage - userage,"years until you retire!")