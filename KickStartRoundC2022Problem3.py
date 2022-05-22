#CodeJam 2022 Round C Problem 3 - Ants on a Stick

cases = int(input())
output = []

class Ant:
    def __init__(self, num, spd, pos):
        self.num = num
        self.spd = spd
        self.pos = pos

for i in range(cases):
    string = "Case #" + str(i+1) + ": "
    n, l = [int(x) for x in input().split()]
    ants = []
    for j in range(n):
        p, d = [int(x) for x in input().split()]
        if d == 0:
            d = -1
        newAnt = Ant(j+1, d, p)

        if len(ants) == 0:
            ants.append(newAnt)
        
        else:
            for k in range(len(ants)):
                if newAnt.pos < ants[k].pos:
                    ants.insert[k, newAnt]
                    break


    while len(ants) > 0:
        falls = []
        for j in range(len(ants)-1):  #sliding window
            #check for collision, 
            print("FIXME:  collisions should include meetings at the 0.5, when positions are one off and they are heading toward one another")
            if ants[j].pos == ants[j+1].pos:
                ants[j].spd *= -1
                ants[j+1].spd *= -1
            
        for j in ants: 
            #advance, pop if fallen
            j.pos += j.spd
            if j.pos > l or j.pos < 0:
                falls.append(j)
        
        for x in falls:
            ants.remove(x)
            string = string + str(x.num) + " "
    
    output.append(string)

for i in range(cases):
    print(output[i])
    


    
