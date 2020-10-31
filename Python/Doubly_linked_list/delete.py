import gc
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

    # function to delete a node from beginning
    def del_beg(self):
        if self.head is not None:
            temp = self.head
            self.head = temp.next
            self.head.prev = None
            temp.next = None
            gc.collect()  # calling garbage collector to free the memory occupied by deleted node

    # function to delete a node with a given key
    def del_key(self, key):
        if self.head is not None:
            temp = self.head
            if temp.data == key:
                self.head = temp.next
                self.head.prev = None
                temp.next = None
            else:
                while temp.next:
                    if temp.data == key:
                        temp.prev.next = temp.next
                        temp.next.prev = temp.prev
                        temp.next = None
                        temp.prev = None
                        break
                    else:
                        temp = temp.next
                else:
                    if temp.data == key:
                        temp.prev.next = None
                        temp.prev = None
                        temp.next = None
                    else:
                        print("key not found")
                gc.collect()

    # function to delete a node from end
    def del_end(self):
        if self.head is not None:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.prev.next = None
            temp.prev = None
            temp.next = None
            gc.collect()

    # function to delete entire doubly linked list
    def del_list(self):
        if self.head is not None:
            temp = self.head
            while temp.next:
                temp = temp.next
                del temp.prev.data
                temp.prev = None
            del temp.data
            temp = None
            self.head = None

    # function to print the doubly linked list
    def print_list(self):
        if self.head is None:
            print("Empty doubly linked list")
        else:
            temp = self.head
            print("Your doubly linked list is: - ")
            while temp:
                print(temp.data, end=" ")
                temp = temp.next


if __name__ == "__main__":
    my_linked_list = Doubly()  # an empty list is created
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
