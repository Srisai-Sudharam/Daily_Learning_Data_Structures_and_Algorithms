from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def skipMdeleteN(head, M, N) :
	#Your code goes here
    if N == 0 or head is None:
        return head
    if M == 0:
        return None

    temp = head
    delete = head
    while temp is not None:
        m = M-1
        
        
        while m != 0 and temp is not None:
            
            m-=1
            temp = temp.next
            delete = delete.next
        n = N+1
        while n != 0 and delete is not None:
            n-=1
            delete = delete.next
        if temp is not None:
            
            temp.next = delete
            temp = temp.next
            m = M
            n = N
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
