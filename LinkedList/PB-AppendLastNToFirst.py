# You have been given a singly linked list of integers along with an integer 'N'. 
# Write a function to append the last 'N' nodes towards the front of the singly linked list and returns the new head to the list.


# here we used fastpointer and slow pointer approach

from sys import stdin

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def appendLastNToFirst(head, n) :
    if head is None or n == 0:
        return head 
    
    slowPointer = head
    fastPointer = head

    counter = 0
    while(counter < n):
        fastPointer = fastPointer.next
        counter+=1
    
    while(fastPointer.next is not None):
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next 
    
    newHead = slowPointer.next
    fastPointer.next = head
    slowPointer.next = None

    return newHead






















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



def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    head = takeInput()
    n = int(stdin.readline().rstrip())

    head = appendLastNToFirst(head, n)
    printLinkedList(head)

    t -= 1 