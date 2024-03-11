class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Stack:

    def __init__(self):
        self.__head = None
        self.__count = 0
    
    def push(self, data):
        n = Node(data)
        n.next = self.__head
        self.__head = n
        self.__count+=1
    
    def pop(self):
        if self.isEmpty():
            return 
        data = self.__head.data
        self.__head = self.__head.next
        self.__count-=1
        return data

    def top(self):
        return self.__head.data

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size == 0
        

# s = Stack()
# s.push(1)
# s.push(2)
# print(s.pop()) #2
# print(s.top()) #1
# print(s.size()) #1
# print(s.isEmpty()) # False

