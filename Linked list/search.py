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

    # method to search an element iteratively
    def search_iter(self, ele):
        temp = self.head
        pos = 1
        while temp:
            if temp.data == ele:
                return "Element found at position",pos
            else:
                temp = temp.next
                pos += 1
        else:
            return "Element not found"

    # method to search an element recursively
    def search_rec(self, node, ele, pos):
        if node is None:
            return "Element not found"
        if node.data == ele:
            return "Element found at position",pos
        return self.search_rec(node.next, ele, pos+1)


if __name__ == "__main__":
    li = LList()
    li.push(1)
    li.push(2)
    li.push(3)
    li.push(4)
    key = 2
    print("Searching key iteratively: - ")
    print(li.search_iter(key))
    print("Searching key recursively: - ")
    print(li.search_rec(li.head, key, 1))

