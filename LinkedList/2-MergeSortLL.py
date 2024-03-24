from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
def midPoint(head) :
    # Write your code here
    slow = head
    fast = head
    if fast is None:
        return None
    while (fast.next is not None) and (fast.next.next is not None):
        slow = slow.next
        fast = fast.next.next
        
    return slow


def merge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    fh = None
    ft = None
    
    if head1.data<head2.data:
        fh = head1
        ft = head1
        head1 = head1.next
    else:
        fh = head2
        ft = head2
        head2 = head2.next
        
    while head1 is not None and head2 is not None:
              
        if head1.data<head2.data:
            ft.next = head1
            head1 = head1.next
            ft = ft.next
        else:
            ft.next = head2
            head2 = head2.next
            ft = ft.next
        
    if head1 is not None:
        ft.next = head1
    if head2 is not None:
        ft.next = head2
    return fh
    


def mergeSort(head) :
    if head is None or head.next is None:
        return head
    mid = midPoint(head)
    h2 = mid.next
    mid.next = None
    l1 = mergeSort(head)
    l2 = mergeSort(h2)
    return merge(l1, l2)
    
    




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

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1