
from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def midPoint(head):
    slow = head 
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverseLinkedList(head):
    if head is None or head.next is None:
        return head
    newHead = reverseLinkedList(head.next)
    head.next.next = head
    head.next = None
    return newHead

def isPalindrome(head) :
    #Your code goes here
    
        
    if head is None or head.next is None:
        return True
    
    mid = midPoint(head) 
    reverseHead = reverseLinkedList(mid.next)

    p1 = head
    p2 = reverseHead
    while p1 is not None and p2 is not None:
        if p1.data != p2.data:
            return False
        p1 = p1.next
        p2 = p2.next
    
    return True
    

































#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    
    if isPalindrome(head) :
        print('true')
    else :
        print('false')
        
    t -= 1