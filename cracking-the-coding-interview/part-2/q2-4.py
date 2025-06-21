"""
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""
from singly_linkedlist import SinglyLinkedList

# Test cases including edge cases
def test_partition():
    # Create a linked list: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
    linked_list = SinglyLinkedList()
    for val in [3, 5, 8, 5, 10, 2, 1]:
        linked_list.add_node(val)

    print("Original linked list: ", end=" ")
    linked_list.print_linked_list()

    # Partition around value 5
    linked_list.make_partition_optimal(5)

    # Validate that all values < 5 appear before any value >= 5
    current = linked_list.head
    partition_val = 5
    seen_gte_partition = False

    while current:
        if current.val >= partition_val:
            seen_gte_partition = True
        elif seen_gte_partition and current.val < partition_val:
            linked_list.print_linked_list()
            raise AssertionError(
                f"Partition violated: found {current.val} after a value >= {partition_val}"
            )
        current = current.next

    print("Partitioning is valid ✅")

def main():
    test_partition()
    print("All tests passed!")

if __name__ == "__main__":
    main()
