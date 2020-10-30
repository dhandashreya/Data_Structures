# class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# class to create a doubly linked list
class Doubly:
    # constructor to create empty doubly linked list
    def __init__(self):
        self.head = None

    # function to add a node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)  # creating a new node and inserting data in it
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head  # next of new_node will point to head
            self.head.prev = new_node  # previous of head will point to new node
            self.head = new_node       # head will point to the new node

    # function to add a node after a given key
    def add_after_key(self, new_data):
        new_node = Node(new_data)  # creating a new node and inserting data in it
        if self.head is None:
            self.head = new_node  # new node is added in the beginning
        else:
            key = int(input("Enter key:-"))
            print("your key is:-", key)
            temp = self.head
            while temp.next:
                if temp.data == key:
                    new_node.next = temp.next
                    new_node.prev = temp
                    temp.next.prev = new_node
                    temp.next = new_node
                    break
                else:
                    temp = temp.next
            if temp.next is None:
                temp.next = new_node
                new_node.prev = temp

    # function to add a node before a given key
    def add_before_key(self, new_data):
        new_node = Node(new_data)
        # when list is empty
        if self.head is None:
            self.head = new_node
        else:
            key = int(input("Enter key:-"))
            temp = self.head
            if temp.data == key:
                new_node.next = temp
                temp.prev = new_node
                self.head = new_node
                return
            while temp.next:
                if temp.data == key:
                    new_node.next = temp
                    new_node.prev = temp.prev
                    temp.prev.next = new_node
                    temp.prev = new_node
                    break
                else:
                    temp = temp.next
            if temp.next is None:
                temp.next = new_node
                new_node.prev = temp

    # function to add a node at the end of doubly linked list
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    # function to print the doubly linked list
    def print_list(self):
        temp = self.head
        print("Your doubly linked list is: - ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == "__main__":
    my_linked_list = Doubly()  # an empty list is created
    print("Press the following to perform the respective operations on doubly linked list: -")
    print("1 : To add a node in the beginning ")
    print("2 : To add a node after a given key")
    print("3 : To add a before a given key")
    print("4 : To add a node at the end")
    print("5 : To print the doubly linked list")
    print("-1 : To stop")
    user_choice = int(input("Enter your choice:-"))
    while user_choice != -1:
        if user_choice == 1:
            my_linked_list.push(int(input("Enter data:-")))
        elif user_choice == 2:
            my_linked_list.add_after_key(int(input("Enter data:-")))
        elif user_choice == 3:
            my_linked_list.add_before_key(int(input("Enter data:-")))
        elif user_choice == 4:
            my_linked_list.append(int(input("Enter data:-")))
        elif user_choice == 5:
            my_linked_list.print_list()
        print()
        user_choice = int(input("Enter your choice:-"))
