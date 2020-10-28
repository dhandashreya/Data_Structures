class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.flag = 0


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

    # function to detect a loop
    def detect_loop_one(self):
        if self.head is None:
            return False
        temp = self.head
        s = set()
        while temp:
            if temp in s:
                return True
            else:
                s.add(temp)
                temp = temp.next
        return False

    def detect_loop_two(self):
        if self.head is None:
            return False
        temp = self.head
        while temp:
            if temp.flag == 1:
                return True
            temp.flag = 1  # suggests that node is already visited
            temp = temp.next
        return False

    # detecting loop using floyd's cycle finding algorithm
    def detect_loop_three(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    my_linked_list = LList()
    my_linked_list.push(3)
    my_linked_list.push(1)
    my_linked_list.push(2)
    my_linked_list.push(4)
    my_linked_list.head.next.next = my_linked_list.head
    print("Detecting loop using method 1")
    if my_linked_list.detect_loop_one():
        print("Loop Exists")
    else:
        print("There is no loop")
    print("Detecting loop using method 2")
    if my_linked_list.detect_loop_two():
        print("Loop Exists")
    else:
        print("There is no loop")
    print("Detecting loop using method 3")
    if my_linked_list.detect_loop_three():
        print("Loop Exists")
    else:
        print("There is no loop")
