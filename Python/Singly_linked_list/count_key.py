class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LList:
    def __init__(self):
        self.head = None

    # function to add node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # counting the occurrences of key iteratively
    def count_iterative(self, key):
        temp = self.head
        count = 0
        if temp is None:
            return 0
        else:
            while temp:
                if temp.data == key:
                    count += 1
                temp = temp.next
            return count

    # counting the occurrences of key recursively
    def count_recursive(self, node, key):
        temp = node
        # base case
        if temp is None:
            return 0
        if temp.data == key:
            return 1 + self.count_recursive(node.next, key)
        return self.count_recursive(node.next, key)


if __name__ == "__main__":
    my_linked_list = LList()
    my_linked_list.push(3)
    my_linked_list.push(1)
    my_linked_list.push(2)
    my_linked_list.push(1)
    my_linked_list.push(2)
    my_linked_list.push(1)
    k = 1
    print("count of k in linked list iteratively", my_linked_list.count_iterative(k))
    print("count of k in linked list recursively", my_linked_list.count_recursive(my_linked_list.head, k))
