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

    # finding middle of linked list using naive approach
    def middle_naive(self):
        temp = self.head
        count = 0
        ptr = 0
        if self.head:
            # traversing first time to know the length of linked list
            while temp:
                count += 1
                temp = temp.next
            temp = self.head
            # traversing second time to reach the middle element
            while ptr != (count//2):
                temp = temp.next
                ptr += 1
        return temp.data

    # finding middle element using two references
    def middle_two(self):
        slow = self.head
        fast = self.head
        if self.head:
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
        return slow.data


if __name__ == "__main__":
    my_linked_list = LList()
    my_linked_list.push(1)
    my_linked_list.push(2)
    my_linked_list.push(3)
    my_linked_list.push(4)
    my_linked_list.push(5)
    my_linked_list.push(6)
    print("Finding middle element using naive approach", my_linked_list.middle_naive())
    print("Finding middle element using second method", my_linked_list.middle_two())
