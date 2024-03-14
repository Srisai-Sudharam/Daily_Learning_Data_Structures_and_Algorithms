class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, data): #O(n) 
        while(len(self.s1) != 0):
            self.s2.append(self.s1.pop())
        self.s1.append(data)
        while(len(self.s2) != 0):
            self.s1.append(self.s2.pop())
    
    def dequeue(self): #O(1)
        if self.isEmpty():
            return
        return self.s1.pop()
    
    def front(self):
        if self.isEmpty():
            return
        return self.s1[-1]
    
    def size(self):
        return len(self.s1)
    
    def isEmpty(self):
        return self.size() == 0
    
q  = Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
while(not q.isEmpty()):
    print(q.dequeue())

q.enqueue(5)
q.enqueue(6)

while(not q.isEmpty()):
    print(q.dequeue())
