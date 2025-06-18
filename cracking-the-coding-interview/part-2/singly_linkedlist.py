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

    def print_linked_list(self):
        current_node = self.head
        while current_node is not None:
            print(f"{current_node.val} =>", end=" ")
            current_node = current_node.next
        print("None")

    """
    Question 2.1: Remove Dups: Write code to remove duplicates from an unsorted linked list.
    How would you solve this problem if a temporary buffer is not allowed?
    """

    "Time Complexity: O(n), Space Complexity: O(n)"
    def remove_dups(self) -> None:
        seen = set()
        current = self.head
        previous = None

        while current:
            if current.val in seen:
                previous.next = current.next
            else:
                seen.add(current.val)
                previous = current
            current = current.next

    "Time Complexity: O(n^2), Space Complexity: O(1)"
    def remove_dups_no_buffer(self) -> None:
        current = self.head

        while current:
            compared_node = current.next
            previous_node = current
            while compared_node:
                if current.val == compared_node.val:
                    previous_node.next = compared_node.next
                else:
                    previous_node = compared_node
                compared_node = compared_node.next
            current = current.next