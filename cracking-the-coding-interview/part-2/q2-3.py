"""
Question 2.3: Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
lnput:the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a ->b->d->e->f
"""

from singly_linkedlist import SinglyLinkedList

# Test cases including edge cases
def test_delete_middle_node():
    # Create a linked list: a -> b -> c -> d -> e -> f
    linked_list = SinglyLinkedList()
    linked_list.add_node('a')
    linked_list.add_node('b')
    middle_node = linked_list.add_node('c')
    linked_list.add_node('d')
    linked_list.add_node('e')
    linked_list.add_node('f')

    print("The linklist: ",end=" ")
    linked_list.print_linked_list()

    # Delete the middle node 'c'
    linked_list.remove_middle_node(middle_node)

    # Check the new structure of the linked list
    current = linked_list.head
    result = []
    while current:
        result.append(current.val)
        current = current.next

    assert result == ['a', 'b', 'd', 'e', 'f'], f"Expected ['a', 'b', 'd', 'e', 'f'], got {result}"
def main():
    test_delete_middle_node()
    print("All tests passed!") 

if __name__ == "__main__":
    main()
