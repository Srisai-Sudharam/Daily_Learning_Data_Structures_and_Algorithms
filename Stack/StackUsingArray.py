class Stack:
    def __init__(self):
        self.__data = []
    
    def push(self, item):
        self.__data.append(item)
    
    def pop(self):
        if self.isEmpty():
            return 
        return self.__data.pop()

    def top(self):
        if self.isEmpty():
            return 
        return self.__data[-1]

    def size(self):
        return len(self.__data)

    def isEmpty(self):
        return len(self.__data) == 0
    
s = Stack()
s.push(1)
s.push(2)
print(s.pop()) #2
print(s.top()) #1
print(s.size()) #1
print(s.isEmpty()) # False
