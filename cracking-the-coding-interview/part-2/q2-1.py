import singly_linkedlist


"""
Question 2.1: Remove Dups: Write code to remove duplicates from an unsorted linked list.
How would you solve this problem if a temporary buffer is not allowed?
"""

# Test cases including edge cases
def test_remove_dups_no_buffer():
    # Test case 1: Empty list
    linked_list = singly_linkedlist.SinglyLinkedList()
    linked_list.remove_dups_no_buffer()
    assert linked_list.head is None, "Failed on empty list"

    # Test case 2: Single element
    linked_list = singly_linkedlist.SinglyLinkedList()
    linked_list.add_node(1)
    linked_list.remove_dups_no_buffer()
    assert linked_list.head.val == 1 and linked_list.head.next is None, "Failed on single element list"

    # Test case 3: No duplicates
    linked_list = singly_linkedlist.SinglyLinkedList()
    linked_list.add_node(1)
    linked_list.add_node(2)
    linked_list.add_node(3)
    linked_list.remove_dups_no_buffer()
    assert linked_list.head.val == 1 and linked_list.head.next.val == 2 and linked_list.head.next.next.val == 3, "Failed on no duplicates"

    # Test case 4: All duplicates
    linked_list = singly_linkedlist.SinglyLinkedList()
    for _ in range(5):
        linked_list.add_node(1)
    linked_list.remove_dups_no_buffer()
    assert linked_list.head.val == 1 and linked_list.head.next is None, "Failed on all duplicates"

    # Test case 5: Mixed values with duplicates
    linked_list = singly_linkedlist.SinglyLinkedList()
    values = [1, 2, 3, 2, 4, 1]
    for val in values:
        linked_list.add_node(val)
    linked_list.remove_dups_no_buffer()
    
    current = linked_list.head
    expected_values = [1, 2, 3, 4]
    for val in expected_values:
        assert current is not None and current.val == val, f"Failed on mixed values with duplicates at value {val}"
        current = current.next
    assert current is None, "Failed on mixed values with duplicates - extra nodes found"
    print("All test cases passed!")

if __name__ == "__main__":
    test_remove_dups_no_buffer()