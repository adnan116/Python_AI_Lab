##A = [1,2,3,4,5,6]
##
####A.append(7)
##
####A.extend([8,9,10])
##
##A.pop()
##
##print(A.index(2))
##
##A.insert(1,55)
##
##print(A)
##


##class Stack:
##
##    def __init__(self):
##
##        self.stack = []
##
##    def push(self,value):
##        self.stack.append(value)
##
##    def pop(self):
##        self.stack.pop()
##
##    def isEmpty(self):
##        if(len(self.stack) == 0):
##            print("Stack is empty")
##        else:
##            print("Stack is not empty")
##
##    def getSize(self):
##        print("Stack size:",len(self.stack))
##        
##    def printStack(self):
##        print(self.stack)
##
##
##s = Stack()
##
##s.push(2)
##s.push(5)
##s.push(9)
##s.push(7)
##
##s.printStack()
##
##s.pop()
##
##s.printStack()
##
##s.isEmpty()
##
##s.getSize()



##class Queue:
##
##    def __init__(self):
##
##        self.queue = []
##
##    def push(self,value):
##        self.queue.append(value)
##
##    def pop(self):
##        self.queue.pop(0)
##
##    def isEmpty(self):
##        if(len(self.queue) == 0):
##            print("queue is empty")
##        else:
##            print("queue is not empty")
##
##    def getSize(self):
##        print("queue size:",len(self.queue))   
##        
##    def printqueue(self):
##        print(self.queue)
##
##
##q = Queue()
##
##q.push(12)
##q.push(55)
##q.push(39)
##q.push(97)
##
##q.printqueue()
##
##q.pop()
##
##q.printqueue()
##
##q.isEmpty()
##
##q.getSize()

##
##S = {'name':'shohan','age':22}
##
##print(S['age'])
##
####S.has_key('name')
##print('name' in S)
##
##print(S.keys())
##
##print(S.values())
##
##print(S.copy())
##
##S.get('name','asd')
##
##P = {'dept':'CS','id':123}
##S.update(P)
##print(S.values())
##
##print(S.keys())
##
##S.pop('id')
##
##print(S.keys())
##
##print(len(S))
##
##S['name'] = 'Rohan'
##print(S.values())
##
##del S['name']
##print(S.keys())



def f(x):
    return x*x*x

print(dict(map(f, range(2, 25))))



