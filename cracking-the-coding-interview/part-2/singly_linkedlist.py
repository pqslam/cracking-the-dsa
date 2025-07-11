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
        return new_node

    def print_linked_list(self):
        current_node = self.head
        while current_node is not None:
            print(f"{current_node.val} =>", end=" ")
            current_node = current_node.next
        print("None")

    def to_list(self):
        llist = list()
        current_node = self.head
        while current_node:
            llist.append(current_node.val)
            current_node = current_node.next
        return llist

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

    """
    Question 2.2: Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
    """
    """
    Assume that the last element is k=1, the second to last is k=2, and so on.
    """
    "Time Complexity: O(n), Space Complexity: O(1)"
    def return_kth_to_last(self, k):
        # Find the end of the list, keep track of the kth element from the current element
        current_node = self.head
        kth_element = self.head
        while current_node:
            k -= 1
            if k < 0:
                kth_element = kth_element.next
            current_node = current_node.next
        return kth_element.val if kth_element and k <= 0 else None

    """
    Question 2.3: Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
    the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
    that node.
    EXAMPLE
    lnput:the node c from the linked list a->b->c->d->e->f
    Result: nothing is returned, but the new linked list looks like a ->b->d->e->f
    """

    """
    Because we can only access to that node, does that mean the parameter of this function is a node between first and last nodes? 
    Do we need to check that the input node is not first or last?
    """

    def remove_middle_node(self, target_node: Node)->None:
        if target_node.next: #Only process if the target node is not the last one.
                target_node.val = target_node.next.val
                target_node.next = target_node.next.next

    
    """
    Question 2.4: Partition - Write code to partition a linked list around a value x, such that all nodes less than x come
    before all nodes greater than or equal to x. If x is contained within the list the values of x only need
    to be after the elements less than x (see below). The partition element x can appear anywhere in the
    "right partition"; it does not need to appear between the left and right partitions.
    EXAMPLE
    Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
    Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
    """

    # 3 -> 5 -> 1 -> 5 -> 2 -> 10 -> 8 -> 4
    """
    Assume that all elements in the linkedlist are numbers for this question
    From the example -> singly linkedlist
    edge cases: empty, 1 element, all dups
    """

    "Time Complexity: O(n^2), Space Complexity: O(1)"
    def make_partition(self, x: int)->None:
        current_node = self.head
        swap_node = None
        while current_node:
            if current_node.val >= x:
                #Find the next possible position to swap
                swap_node = current_node.next
                while swap_node and swap_node.val >= x: 
                    swap_node = swap_node.next
                if not swap_node: # If the swap_node is None, then we go to the end of the list already.
                    break
                temp_val = current_node.val
                current_node.val = swap_node.val
                swap_node.val = temp_val
            current_node = current_node.next

    "Time Complexity: O(n), Space Complexity: O(1)"
    def make_partition_optimal(self, x: int) -> None:
        current_node = self.head.next if self.head else None
        new_order = self.head
        if new_order:
            new_order.next = None
        while current_node:
            next_node = current_node.next
            current_node.next = None
            if current_node.val >= x:
                new_order.next = current_node
                new_order = current_node
            else:
                current_node.next = self.head
                self.head = current_node 
            current_node = next_node
        
        self.print_linked_list()

    """
    Question 2.5 - Sum Lists: You have two numbers represented by a linked list, where each node contains a single
    digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
    function that adds the two numbers and returns the sum as a linked list.
    EXAMPLE
    Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
    Output: 2 -> 1 -> 9. That is, 912.
    FOLLOW UP
    Suppose the digits are stored in forward order. Repeat the above problem.
    Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
    Output: 9 -> 1 -> 2. That is, 912.
    """

    """
    Possible questions:
    - Do I need to keep num1 and num2? In case that one of them can be updated to became the sum
    """
    
    "Time Complexity: O(m + n), Space Complexity: O(log(sum))"
    def sum_lists_reverse_order(num1: "SinglyLinkedList", num2: "SinglyLinkedList") -> "SinglyLinkedList":
        sum_linkedlist = SinglyLinkedList()
        #convert the linkedlists to numbers
        sum = 0
        if not num1.head and not num2.head:
            return sum_linkedlist
        for llist in [num1, num2]:
            current_node = llist.head
            number = 0
            base = 1
            while current_node:
                number += current_node.val * base
                base = base * 10
                current_node = current_node.next
            sum += number
            
        #convert the sum to linkedlist
        if sum == 0:
            sum_linkedlist.add_node(0)
        else:
            while sum > 0:
                digit = sum % 10
                sum_linkedlist.add_node(digit)
                sum //= 10
        
        return sum_linkedlist
    
    "Time Complexity: O(m + n), Space Complexity: O(log(sum))"
    def sum_lists_forward_order(num1: "SinglyLinkedList", num2: "SinglyLinkedList") -> "SinglyLinkedList":
        sum_linkedlist = SinglyLinkedList()
        sum = 0
        if not num1.head and not num2.head:
            return sum_linkedlist
        else:
            for llist in [num1, num2]:
                number = 0
                current_node = llist.head
                while current_node:
                    number = (number * 10) + current_node.val
                    current_node = current_node.next
                sum = sum + number
            #convert the sum to linkedlist
            if sum == 0:
                sum_linkedlist.add_node(0)
            else:
                for char in str(sum):
                    sum_linkedlist.add_node(int(char))
        return sum_linkedlist
