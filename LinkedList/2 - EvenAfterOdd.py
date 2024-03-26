# For a given singly linked list of integers, arrange the nodes such that all the even number nodes are placed after the all odd number nodes. 
# The relative order of the odd and even terms should remain unchanged.

# Note :
# 1. No need to print the linked list, it has already been taken care. Only return the new head to the list.
# 2. Don't create a new linked list.
# 3.  Just change the data, instead rearrange the provided list.


from sys import stdin


class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def evenAfterOdd(head) :
    if head is None or head.next is None:
        return head
    #Your code goes here
    eh = None
    et = None
    oh = None
    ot = None
    while head is not None:
        if head.data % 2 == 0:
            if eh is None:
                eh = head
                et = head
            else:
                et.next = head
                et = et.next
        else:
            if oh is None:
                oh = head
                ot = head
            else:
                ot.next = head
                ot = ot.next
        head = head.next
    if oh is None:
        return eh
    else:
        ot.next = eh
    if eh is not None:
        et.next = None
    return oh
            
            
























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
    newHead = evenAfterOdd(head)
    printLinkedList(newHead)  
    
    t -= 1