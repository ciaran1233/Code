class gamer:
    def __init__(self):
        self.Name =""
        self.highscore = 0
        
totalnumberofplayers = 5
player = []
for i in range (totalnumberofplayers):
    player.append(gamer())
for i in range (totalnumberofplayers):
    print("enter player",i+1,"name:",end ="")
    player [1].name = input()
    print("enter player",i+1,"high score :",end ="")
    player[i].highscore = input ()
    
player.sort(key = lambda x : x.highscore,reverse = True)
for i in range(totalnumberofplayers):
    print("player",player[i].Name,"has a score of ",player[i].highscore)