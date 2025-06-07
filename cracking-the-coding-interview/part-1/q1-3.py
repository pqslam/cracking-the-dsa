"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
"""

"Time complexity: O(n) where n is the length of the input string"
"Space complexity: O(n) since we are creating a new string for the result"
def urlify(input: str, length: int) -> str:
    if len(input) != length:
        input = input.rstrip()
    return input.replace(" ","%20")

# Trying to reduce the space complexity
"Time complexity: O(n) where n is the length of the input string"
"Space complexity: O(1) since we are modifying the input string in place"
def urlify_optimal(input: list, length: int) -> None:
    del input[length:]
    num_space = 0
    for idx in range(0, length):
        if input[idx] == " ":
            num_space += 1
    insert_idx = length + num_space * 2
    while len(input) < length + num_space * 2:
        input.append("")  # Ensure the list has enough space
    for idx in range(length - 1, -1, -1):
        if input[idx] == " ":
            input[insert_idx - 1] = "0"
            input[insert_idx - 2] = "2"
            input[insert_idx - 3] = "%"
            insert_idx -= 3
        else:
            input[insert_idx - 1] = input[idx]
            insert_idx -= 1


# Test cases including edge cases
def run_tests(func):
    tests = [
        ("Mr John Smith    ", 13, "Mr%20John%20Smith"),
        ("HelloWorld", 10, "HelloWorld"),
        ("     ", 5, "%20%20%20%20%20"),
        (" Hello", 6, "%20Hello"),
        ("Hello ", 6, "Hello%20"),
        ("Hi  there     ", 9, "Hi%20%20there"),
        ("A", 1, "A"),
        (" ", 1, "%20"),
        ("", 0, ""),
        ("Test Me      ", 7, "Test%20Me")
    ]
    
    for input_str, length, expected in tests:
        if func == urlify_optimal:
            input_str = list(input_str)
            func(input_str, length)
            print(input_str)
            assert ''.join(input_str) == expected
        else:
            assert func(input_str, length) == expected
    print(f"All test cases for {func.__name__} passed!")
if __name__ == "__main__":
    run_tests(urlify)
    run_tests(urlify_optimal)
    print("Function is working correctly.")