print("Welcome to Treasure Island, a choose-your-own-adventure game.")
print("Legend has it that there is some buried treasure on the island you are exploring… so you have decided to in search for it.")

def game():
    swim_or_wait = input("You come to a lake. Do you either want to wait for a boat, or swim across? (swim/wait): ")
    
if swim_or_wait == "swim":
    print("You get eaten by a hungry shark. Game over.")
elif swim_or_wait == "wait":
    print("A boat arrives and you arrive at the island safely.")
    cave_or_stay = input("You come to a cave, do you want to venture inside or walk on? (venture/walk): ")
    
if cave_or_stay == "venture":
    print("You are squished by boulders never to be seen again. Game over.")
elif cave_or_stay == "walk":
    print("You walk away from the cave along a narrow track in the forest.")
    
    crossroad_turn = input("You eventually reach a crossroads. Do you want to go left, right or straight? (left/right/straight): ")
    
if crossroad_turn == "left":
    print("You are trampled by a herd of wildebeest. Game over.")
elif crossroad_turn == "straight":
    print("You get stung by a poisonous wasp. Game over.")
elif crossroad_turn == "right":
    print("You march on and find the treasure, wahoo!")
    
    
print(ASCII_ART)
game()