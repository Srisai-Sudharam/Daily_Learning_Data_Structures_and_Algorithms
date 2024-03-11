import queue
stack = [1, 2, 3, 4]
stack.append(5)
stack.pop()

# you can use default list data structure for stack

# in case of queue you can use built in queue library

# q = queue.Queue()

# q.put(1)
# q.put(2)
# q.put(3)

# while(not q.empty()):
#     print(q.get())

# there is another class in queue which will behave like a list

# q = queue.LifoQueue()
# q.put(1)
# q.put(2)
# q.put(3)

# while(not q.empty()):
#     print(q.get())