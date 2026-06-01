# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Global head
head = None

def insertNodeAtTheBeggining(data):
    global head
    newNode = Node(data)
    newNode.next = head
    head = newNode

def insertNodeAtTheEnd(data):
    global head
    newNode = Node(data)

    if head is None:
        head = newNode
    else:
        current = head
        while current.next:
            current = current.next
        current.next = newNode

def traverseLinkedList():
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("Statue!!")

def insertNodeafterGivenNode(data, node):
    global head
    current = head

    while current:
        if current.data == node:
            newNode = Node(data)
            newNode.next = current.next
            current.next = newNode
            return
        current = current.next

    print("The node does not exist")


# -------------------------
# TEST DATA
insertNodeAtTheBeggining("LET ME THE ONE")
insertNodeAtTheBeggining("ALL or NOTHING")
insertNodeAtTheBeggining("magaan naba ang iyong pag hinga")
insertNodeAtTheBeggining("PUSONG KIGAW")

insertNodeAtTheEnd("Araw Gabi by Soul Jazz Cover")
insertNodeAtTheEnd("B4 I LET YOU GO")

insertNodeafterGivenNode("Sining","Empilight")


print("Final List:")
traverseLinkedList()
