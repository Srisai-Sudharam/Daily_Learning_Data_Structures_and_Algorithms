from sys import stdin


class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def swapNodes(head, i, j) :
    if head is None or i == j:
        return head
	#Your code goes here
    m = 0 #name 
    curr = head
    while(m < i -1):
        curr = curr.next
        m += 1
    first = curr


    n = 0
    curr = head
    while(n < j-1):
        curr = curr.next 
        n+=1
    second = curr

    node1 = first.next 
    node2 = second.next

    if node1.next == node2:
        first.next = node2
        node1.next = node2.next
        node2.next = node1
    else:
        node1.next = second.next.next
        second.next = node1
        node2.next = first.next.next
        first.next = node2
    
    return head
        




























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
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1