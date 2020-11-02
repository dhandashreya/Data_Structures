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
            self.head = new_node  # head points to new node

    # method to remove duplicates in a sorted linked list
    def remove_duplicates(self):
        temp = self.head
        if self.head is None or self.head.next is None:
            return
        else:
            while temp.next:
                if temp.data == temp.next.data:
                    del temp.next.data
                    temp.next = temp.next.next
                else:
                    temp = temp.next

    # method to print the linked list
    def print_list(self):
        temp = self.head
        print("Your linked list is: - ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == "__main__":
    my_linked_list = LList()
    my_linked_list.push(11)
    my_linked_list.push(11)
    my_linked_list.push(11)
    my_linked_list.push(21)
    my_linked_list.push(43)
    my_linked_list.push(43)
    my_linked_list.push(60)
    print("Before removing duplicates")
    my_linked_list.print_list()
    print()
    my_linked_list.remove_duplicates()
    print("After removing duplicates")
    my_linked_list.print_list()
