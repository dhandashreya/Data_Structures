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
            self.head = new_node # head points to new node

    # method to delete node from the beginning
    def del_beg(self):
        if self.head is not None:
            temp = self.head
            self.head = temp.next
            temp = None

    # method to delete a node with the given key as data
    def del_key(self, key):
        if self.head is not None:
            temp = self.head  # pointing to head
            ctr = temp.next  # pointing to the second node
            if temp.data == key:
                self.head = ctr
                temp = None
            else:
                while ctr and ctr.data != key:
                    temp = ctr
                    ctr = ctr.next
                if ctr is not None:
                    temp.next = ctr.next
                    ctr = None
                else:
                    print("key not present in the linked list")

    # method to delete a node from the end
    def del_end(self):
        if self.head is not None:
            temp = self.head
            ctr = temp.next
            while ctr.next:
                temp = ctr
                ctr = ctr.next
            ctr = None
            temp.next = None

    # method to delete entire linked list
    def del_list(self):
        if self.head is not None:
            temp = self.head
            while temp:
                ctr = temp.next
                del temp.data
                temp = ctr

    # method to print the linked list
    def print_list(self):
        if self.head is not None:
            temp = self.head
            print("Your linked list is: - ")
            while temp:
                print(temp.data, end=" ")
                temp = temp.next


if __name__ == "__main__":
    my_linked_list = LList()  # an empty list is created
    print("Press the following to perform the respective operations on linked list: -")
    print("1 : To add a node in the beginning ")
    print("2 : To delete a node from beginning")
    print("3 : To delete a node with a given key")
    print("4 : To delete a node from end")
    print("5 : To delete entire linked list")
    print("6 : To print the linked list")
    print("-1 : To stop")
    user_choice = int(input("Enter your choice:-"))
    while user_choice != -1:
        if user_choice == 1:
            my_linked_list.push(int(input("Enter data:-")))
        elif user_choice == 2:
            my_linked_list.del_beg()
        elif user_choice == 3:
            my_linked_list.del_key(int(input("Enter any key")))
        elif user_choice == 4:
            my_linked_list.del_end()
        elif user_choice == 5:
            my_linked_list.del_list()
        elif user_choice == 6:
            my_linked_list.print_list()
        print()
        user_choice = int(input("Enter your choice:-"))
