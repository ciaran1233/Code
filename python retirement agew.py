def getName():
  name = raw_input("What is your name?: ")
  return name

def getAge():
  age = input("How old are you?: ")
  return int(age)

def ifOrNot():
  retirementAge = 65
  myAge = getAge()
  if(myAge >= retirementAge):
    print("Hello  ",getName(), ", you are at the  retirment age")
  else:
    timeToRetirement = retirementAge - myAge
    print("Hello ", getName(), " you are not at the retirement age, you need to wait ", timeToRetirement, " more")

def main():
  ifOrNot()

def ifOrNot():
    retirementAge = 65
    name = getName()
    age = getAge()
    if (age >= retirementAge):
        print("Hello  ", name, ", are you in retirment age")
    else:
        timeToRetirement = retirementAge - age
        print("Hello ", getName(), " are you not in retirement age, you need to wait ",)
        
print()