# You have been given a singly linked list of integers. 
# Write a function to print the list in a reverse order.

from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def printReverse(head) :
    #Your code goes here
    if head is None:
        return
    printReverse(head.next)
    print(head.data, end = " ")






























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
    printReverse(head)
    print()

    t -= 1