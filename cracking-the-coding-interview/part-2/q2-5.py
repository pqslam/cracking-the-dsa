from singly_linkedlist import SinglyLinkedList

def test_sum_lists():
    test_cases = [
        # Reverse-order cases
        {
            "input1": [7, 1, 6],
            "input2": [5, 9, 2],
            "expected": [2, 1, 9],
            "description": "Normal case with reverse order",
            "mode": "reverse"
        },
        {
            "input1": [],
            "input2": [5, 9, 2],
            "expected": [5, 9, 2],
            "description": "First list empty (reverse)",
            "mode": "reverse"
        },
        {
            "input1": [7, 1, 6],
            "input2": [],
            "expected": [7, 1, 6],
            "description": "Second list empty (reverse)",
            "mode": "reverse"
        },
        {
            "input1": [],
            "input2": [],
            "expected": [],
            "description": "Both lists empty (reverse)",
            "mode": "reverse"
        },
        {
            "input1": [0],
            "input2": [0],
            "expected": [0],
            "description": "Both lists with single zero (reverse)",
            "mode": "reverse"
        },
        {
            "input1": [9, 9, 9],
            "input2": [1],
            "expected": [0, 0, 0, 1],
            "description": "Carry over case (reverse)",
            "mode": "reverse"
        },

        # Forward-order cases
        {
            "input1": [6, 1, 7],
            "input2": [2, 9, 5],
            "expected": [9, 1, 2],
            "description": "Normal case with forward order",
            "mode": "forward"
        },
        {
            "input1": [0],
            "input2": [0],
            "expected": [0],
            "description": "Both lists with single zero (forward)",
            "mode": "forward"
        },
        {
            "input1": [9, 9, 9],
            "input2": [1],
            "expected": [1, 0, 0, 0],
            "description": "Carry over case (forward)",
            "mode": "forward"
        },
        {
            "input1": [],
            "input2": [5, 9, 2],
            "expected": [5, 9, 2],
            "description": "First list empty (forward)",
            "mode": "forward"
        }
    ]

    for case in test_cases:
        list1 = SinglyLinkedList()
        list2 = SinglyLinkedList()

        for val in case["input1"]:
            list1.add_node(val)
        for val in case["input2"]:
            list2.add_node(val)

        if case["mode"] == "reverse":
            result = SinglyLinkedList.sum_lists_reverse_order(list1, list2)
        elif case["mode"] == "forward":
            result = SinglyLinkedList.sum_lists_forward_order(list1, list2)
        else:
            raise ValueError("Unknown mode in test case")

        result_list = result.to_list() if result else []
        assert result_list == case["expected"], f"Failed for {case['description']}: expected {case['expected']}, got {result_list}"

    print("All test cases passed ✅")

if __name__ == "__main__":
    test_sum_lists()
