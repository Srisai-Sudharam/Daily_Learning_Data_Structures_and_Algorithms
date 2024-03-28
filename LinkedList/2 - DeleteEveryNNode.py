# You have been given a singly linked list of integers along with two integers, 'M,' and 'N.' 
# Traverse the linked list such that you retain the 'M' nodes, then delete the next 'N' nodes. 
# Continue the same until the end of the linked list. Indexing starts from 1.

# To put it in other words, in the given linked list, you need to delete N nodes after every M nodes.

# Note :
# No need to print the list, it has already been taken care. Only return the new head to the list. You can return null in case where all nodes will be deleted.


from sys import stdin


class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def skipMdeleteN(head, M, N) :
	#Your code goes here
    
    if M == 0 or head is None:
        return None
    
    if N == 0:
        return head
    
    curr = head
    tail = None

    while curr is not None:
        keep = 0
        while curr is not None and keep < m:
            if tail is None:
                tail = curr
            else:
                tail.next = curr
                tail = tail.next 
            curr = curr.next
            keep+=1

        skip = 0
        while curr is not None and skip < n:
            curr = curr.next
            skip+=1 
    

    if tail is not None:
        tail.next = None
    
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
    m_n = stdin.readline().strip().split(" ")

    m = int(m_n[0])
    n = int(m_n[1])

    newHead = skipMdeleteN(head, m, n)
    printLinkedList(newHead)

    t -= 1

# 1
# 10 22 10 26 11 7 8 1 23 5 1 28 0 -1
# 2 3
    
# 1
# 10 22 10 26 11 7 8 1 23 5 1 -1
# 2 3