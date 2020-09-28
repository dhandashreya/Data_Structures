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

    # method to count number of nodes iteratively
    def get_count(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    # method to calculate number of nodes recursively
    def get_count_rec(self, node):
        if node is None:  # Base case
            return 0
        else:
            return 1 + self.get_count_rec(node.next)

    def count_rec(self):
        return self.get_count_rec(self.head)


if __name__ == "__main__":
    my_linked_list = LList()
    my_linked_list.push(1)
    my_linked_list.push(2)
    my_linked_list.push(3)
    my_linked_list.push(4)
    my_linked_list.push(5)
    print("Number of nodes in linked list counted iteratively:", my_linked_list.get_count())
    print("Number of nodes in linked list counted recursively:", my_linked_list.count_rec())
