from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def reverseLinkedListRec(head) :
    
	#Your code goes here
    if head is None:
        return 
    if head.next is None:
        return head
    
    newHead = reverseLinkedListRec(head.next)
    curr = newHead
    while(curr.next is not None):
        curr = curr.next
    
    curr.next = head
    head.next = None

    return newHead





























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




def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()

    newHead = reverseLinkedListRec(head)
    printLinkedList(newHead)

    t -= 1


# 1
# 1 2 3 4 5 6 7 8 9 -1