class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LList:
    def __init__(self):
        self.head = None

    # method to add a node in the beginning of the linked list
    def push(self, new_data):
        new_node = Node(new_data)  # new node is created and data is given to it
        # when linked is empty
        if self.head is None:
            self.head = new_node
        # when linked list is non empty
        else:
            new_node.next = self.head  # new node's next point to head
            self.head = new_node   # head points to new node

    # determining whether a list is palindrome by using stack
    def palindrome(self, head):
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
    my_linked_list = LList()
    my_linked_list.push(1)
    my_linked_list.push(2)
    my_linked_list.push(3)
    my_linked_list.push(4)
    my_linked_list.push(3)
    my_linked_list.push(2)
    my_linked_list.push(1)
    print("Is my linked list a palindrome", my_linked_list.palindrome(my_linked_list.head))
