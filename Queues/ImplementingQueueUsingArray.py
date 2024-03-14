class Queue:
    def __init__(self):
        self.__arr = []
        self.__front = 0
        self.__count = 0

    def enqueue(self, data):
        self.__arr.append(data)
        self.__count+=1
    def dequeue(self):
        if self.isEmpty():
            return 
        element = self.__arr[self.__front]
        self.__front+=1
        self.__count-=1
        return element

    def front(self):
        if self.isEmpty():
            return
        element = self.__arr[self.__front]
        return element
    def size(self):
        return self.__count
        
    def isEmpty(self):
        return (self.__count == 0)
    


q  = Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
while(not q.isEmpty()):
    print(q.dequeue())
