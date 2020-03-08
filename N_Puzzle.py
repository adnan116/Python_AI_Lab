##row = int(input("Enter The Row Number: "))
##col = int(input("Enter The Column Number: "))

A = [[6,1,10,2],[7,11,4,14],[5,1000,9,15],[8,12,13,3]]
B = []

##for i in range(0,row):
##    B = []
##    for j in range(0,col):
##
##        B.append(int(input("Enter Value: ")))
##
##
##    A.append(B)


print("Board: ",A)

def flatBoard(C):
    one = []
    for i in range(0,len(C)):
        for j in range(0,len(C)):

            one.append(C[i][j])
    return one
print("Flat Board: ",flatBoard(A))

def inversion(I):
    count =0
    for i in range(0,len(I)-1):
        for j in range(i+1,len(I)):
            if(I[i]==1000):
                continue
            elif(I[i]>I[j]):
                count = count+1

    return count

inv = inversion(flatBoard(A))

print("Inversion: ",inv)

def blankPosition(Q):
    for i in range(len(Q)):
        if(1000 in Q[i]):
            p = i+1
                      
    pos = len(Q)-p+1

    return pos


print("Blank Position: ",blankPosition(A))


def checkEven(n):
    if(n%2==0):
        return True
    else:
        return False



print(checkEven(inv))


def solvePossible(W):
    if(checkEven(len(W))==False and checkEven(inversion(flatBoard(W)))==True):
        return "Possible"
    elif(checkEven(len(W))==True and checkEven(blankPosition(W))==False and checkEven(inversion(flatBoard(W)))==True):
        return "Possible"
    elif(checkEven(len(W))==True and checkEven(blankPosition(W))==True and checkEven(inversion(flatBoard(W)))==False):
        return "Possible"
    else:
        return "Not Possible"



print("Possibility: ", solvePossible(A))
