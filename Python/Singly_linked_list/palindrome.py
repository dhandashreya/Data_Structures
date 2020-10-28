class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# determining whether a list is palindrome by using stack
def palindrome(head):
    temp = head
    # declaring a stack
    stack = []
    is_palindrome = True
    while temp is not None:
        stack.append(temp.data)  # pushing all elements to stack
        temp = temp.next
    while head is not None:
        i = stack.pop()  # getting the top most element
        if head.data != i:
            is_palindrome = False
            break
        head = head.next
    return is_palindrome


if __name__ == "__main__":
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(3)
    six = Node(2)
    seven = Node(1)

    one.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = six
    six.next = seven

    result = palindrome(one)
    print("Is linked list a palindrome:", result)
