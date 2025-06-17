class SinglyLinkedList:

    class Node:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None
    
    def add_node(self, val) -> None:
        new_node = self.Node(val)
        if self.head == None:
            self.head = new_node
        else:
            node = self.head
            while node.next != None:
                node = node.next
            node.next = new_node 

    