class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def takeInput(): #O(N^2)
    lis = [int(i) for i in input().split()]
    head = None
    for i in lis:
        if i == -1:
            break
        
        newNode = Node(i)

        if head is None:
            head = newNode
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode


    return head

def takeInputOptimised(): #O(N)
    #here we are using tail pointer
    lis = [int(i) for i in input().split()]
    head = None
    tail = None
    for i in lis:
        if i == -1:
            break

        newNode = Node(i)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = tail.next
    return head


        
def printLinkedList(head):
    while head is not None:
        print(head.data, "-->", sep = "", end = "")
        head = head.next
    print("None")

def length(head):
    count = 0
    while head is not None:
        head = head.next
        count+=1
    return count


def insertAtIthPosition(head, index, data):
    if index < 0 or index > length(head):
        return head
    prev = None
    curr = head
    count = 0
    while(count < index):
        prev = curr
        curr = curr.next
        count+=1
    
    newNode = Node(data)
    if prev is None:
        head = newNode
        
    else:
        prev.next = newNode
    
    newNode.next = curr
    return head


def insertAtIthRecursive(head, index, data):
    if head is None or index < 0 :
        return head
    if index == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode
    head.next = insertAtIthRecursive(head.next, index - 1, data)
    return head



ll = takeInputOptimised()
printLinkedList(insertAtIthRecursive(ll, 7, 12))
