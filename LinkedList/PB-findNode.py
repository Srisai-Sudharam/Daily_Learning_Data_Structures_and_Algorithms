# You have been given a singly linked list of integers. 
# Write a function that returns the index/position of integer data denoted by 'N' (if it exists). 
# Return -1 otherwise.
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def findNode(head, n) :
    count = 0
    while head is not None:
        if head.data == n:
            return count
        head = head.next 
        count+=1
    return -1