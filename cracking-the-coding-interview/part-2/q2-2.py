"""
Question 2.2: Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
"""

#List of testcases including edge cases
def test_return_kth_to_last():
    from singly_linkedlist import SinglyLinkedList

    # Test case 1: Empty list
    linked_list = SinglyLinkedList()
    assert linked_list.return_kth_to_last(1) is None, "Failed on empty list"

    # Test case 2: Single element
    linked_list = SinglyLinkedList()
    linked_list.add_node(1)
    assert linked_list.return_kth_to_last(1) == 1, "Failed on single element list"

    # Test case 3: Two elements, k=1
    linked_list = SinglyLinkedList()
    linked_list.add_node(1)
    linked_list.add_node(2)
    assert linked_list.return_kth_to_last(1) == 2, "Failed on two elements with k=1"

    # Test case 4: Two elements, k=2
    assert linked_list.return_kth_to_last(2) == 1, "Failed on two elements with k=2"

    # Test case 5: Multiple elements, k=3
    linked_list = SinglyLinkedList()
    for i in range(5):
        linked_list.add_node(i + 1)
    assert linked_list.return_kth_to_last(3) == 3, "Failed on multiple elements with k=3"

    # Test case 6: k larger than list size
    assert linked_list.return_kth_to_last(10) is None, "Failed when k is larger than list size"

    print("All test cases passed!")
if __name__ == "__main__":
    test_return_kth_to_last()