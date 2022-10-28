# 1.Insert a node at the head of a linked list 

def insertNodeAtHead(llist, data):
    x = SinglyLinkedListNode(data)
    if (llist == None):
        llist = x
    else:
        new_node = x
        new_node.next = llist
        llist = new_node
    return llist
    




# 2.Insert a Node at the Tail of a Linked List

def insertNodeAtTail(head, data):
    if head is None:
        return SinglyLinkedListNode(data)
    x = head
    while x.next is not None:
        x = x.next
    x.next = SinglyLinkedListNode(data)
    return head
