import random


def Fitness(pattern):
    return ((pattern[0]-pattern[1])+(pattern[2]-pattern[3])+(pattern[4]-pattern[5])+(pattern[6]-pattern[7]))


x1 = [9,8,7,6,5,4,3,2]
x2 = [6,5,9,8,3,2,5,4]
x3 = [3,2,5,4,7,6,9,8]
x4 = [2,1,6,5,7,6,5,4]


print("Fitness of X1: ",Fitness(x1))
print("Fitness of X2: ",Fitness(x2))
print("Fitness of X3: ",Fitness(x3))
print("Fitness of X4: ",Fitness(x4))


allFit = [Fitness(x1),Fitness(x2),Fitness(x3),Fitness(x4)]
#print(allFit)

totalFitness = Fitness(x1)+Fitness(x2)+Fitness(x3)+Fitness(x4)


avg = (totalFitness/4)


#print(totalFitness)

def findProbability(x):
    return (x/totalFitness)

prob = [findProbability(allFit[0]),findProbability(allFit[1]),findProbability(allFit[2]),findProbability(allFit[3])]


nTimesProb = [prob[0]*4,prob[1]*4,prob[2]*4,prob[3]*4]

##print(prob)
##print(nTimesProb)


def findRange(stop,start = 0):
    return start+stop
    

x1R = findRange(0.25)
x2R = findRange(0.25,x1R)
x3R = findRange(0.25,x2R)
x4R = findRange(0.25,x3R)


bin = {
    "x1Ra":[0,x1R],
    "x2Ra":[x1R,x2R],
    "x3Ra":[x2R,x3R],
    "x4Ra":[x3R,x4R]
   }

print(bin)

ranNum = [round(random.uniform(0,1),2),round(random.uniform(0,1),2),round(random.uniform(0,1),2),round(random.uniform(0,1),2)]

print(ranNum)

selectedPattern = []

for x in range(4):
    if(bin['x1Ra'][0]<ranNum[x]<bin['x1Ra'][1]):
        selectedPattern.append(x1)
    if(bin['x2Ra'][0]<ranNum[x]<bin['x2Ra'][1]):
        selectedPattern.append(x2)
    if(bin['x3Ra'][0]<ranNum[x]<bin['x3Ra'][1]):
        selectedPattern.append(x3)
    if(bin['x4Ra'][0]<ranNum[x]<bin['x4Ra'][1]):
        selectedPattern.append(x4)

print("\n\nSelected Pattern: ",selectedPattern)



