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

    # method to get nth node iteratively
    def get_iter(self, pos):
        if self.head is not None:
            count = 1
            temp = self.head
            while temp and count != pos:
                temp = temp.next
                count += 1
            if temp and count == pos:
                print(temp.data)
            else:
                print("Node not present")
        else:
            print("Empty list")

    # method to get nth node recursively
    def get_rec(self, node, pos):
        count = 1
        if node is not None:
            if count == pos:
                print(node.data)
            else:
                self.get_rec(node.next, pos-1)
        else:
            print("Node not present")


if __name__ == "__main__":
    li = LList()
    li.push(1)
    li.push(2)
    li.push(3)
    li.push(4)
    print("Getting nth node iteratively: - ")
    li.get_iter(2)
    print("Getting nth node recursively: - ")
    li.get_rec(li.head, 2)
