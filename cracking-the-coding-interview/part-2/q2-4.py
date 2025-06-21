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

def assert_partition_is_valid(linked_list, partition_val):
    current = linked_list.head
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

# Test cases including edge cases
def test_partition():
    test_cases = [
        {
            "input": [3, 5, 8, 5, 10, 2, 1],
            "partition": 5,
            "description": "Normal mixed values"
        },
        {
            "input": [],
            "partition": 5,
            "description": "Empty list"
        },
        {
            "input": [1, 2, 3],
            "partition": 5,
            "description": "All values less than partition"
        },
        {
            "input": [5, 6, 7],
            "partition": 5,
            "description": "All values greater than or equal to partition"
        },
        {
            "input": [5],
            "partition": 5,
            "description": "Single node equal to partition"
        },
        {
            "input": [1],
            "partition": 5,
            "description": "Single node less than partition"
        },
        {
            "input": [10, 9, 8, 7, 6],
            "partition": 5,
            "description": "All nodes greater than partition, descending order"
        },
        {
            "input": [2, 1, 0, -1, -5],
            "partition": 5,
            "description": "All nodes less than partition, descending order"
        }
    ]

    for case in test_cases:
        print(f"\nTesting case: {case['description']}")
        linked_list = SinglyLinkedList()
        for val in case["input"]:
            linked_list.add_node(val)
        print("Original linked list: ", end=" ")
        linked_list.print_linked_list()

        linked_list.make_partition_optimal(case["partition"])
        assert_partition_is_valid(linked_list, case["partition"])

def main():
    test_partition()
    print("\nAll tests passed! ✅")

if __name__ == "__main__":
    main()
