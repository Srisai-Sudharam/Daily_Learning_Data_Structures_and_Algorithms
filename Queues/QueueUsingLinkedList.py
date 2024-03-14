


class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0
    
    def enqueue(self, data):
        node = Node(data)
        if self.__head is None: #edge case (handled) try running using __head and __tail and observe how __tail pointer is poiniting after removal of all elements
            self.__head = node
            self.__tail = node
        else:
            self.__tail.next = node
            self.__tail = self.__tail.next
        self.__count+=1

    def dequeue(self):
        if self.isEmpty():
            return 
        element = self.__head.data
        self.__head = self.__head.next
        self.__count-=1
        return element
    
    def front(self):
        if self.isEmpty():
            return 
        return self.__head.data
    
    def size(self):
        return self.__count
    
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
