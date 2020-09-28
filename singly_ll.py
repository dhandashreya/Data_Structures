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

    # method to add a node after a certain key
    def add_after_key(self, new_data):
        new_node = Node(new_data)  # new node is created and data is given to it
        # when linked is empty
        if self.head is None:
            self.head = new_node
        # when linked list is non empty
        else:
            key = int(input("Enter key:-"))
            temp = self.head
            while temp:
                if temp.data == key:
                    new_node.next = temp.next
                    temp.next = new_node
                    break
                else:
                    temp = temp.next
                    if temp.next is None:
                        temp.next = new_node
                        break

    # method to add a node at the end of the linked list
    def append(self, new_data):
        new_node = Node(new_data)  # new node is created and data is given to it
        # when linked is empty
        if self.head is None:
            self.head = new_node
        # when linked list is non empty
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # method to print the linked list
    def print_list(self):
        temp = self.head
        print("Your linked list is: - ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == "__main__":
    my_linked_list = LList()  # an empty list is created
    print("Press the following to perform the respective operations on linked list: -")
    print("1 : To add a node in the beginning ")
    print("2 : To add a node after a given key")
    print("3 : To add a node at the end")
    print("4 : To print the linked list")
    print("-1 : To stop")
    user_choice = int(input("Enter your choice:-"))
    while user_choice != -1:
        if user_choice == 1:
            my_linked_list.push(int(input("Enter data:-")))
        elif user_choice == 2:
            my_linked_list.add_after_key(int(input("Enter data:-")))
        elif user_choice == 3:
            my_linked_list.append(int(input("Enter data:-")))
        elif user_choice == 4:
            my_linked_list.print_list()
        print()
        user_choice = int(input("Enter your choice:-"))
