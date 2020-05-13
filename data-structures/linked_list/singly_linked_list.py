# class node --> data, next
# class LinkedList --> just contains head == (data, next)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    # def __init__(self):
    #     self.head = None

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while nodes is not None:
            nodes.append(node.data)
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def is_list_empty(self):
        return True if self.head is None else False

    def list_length(self):
        curr_node = self.head
        length = 0
        while curr_node is not None:
            curr_node = curr_node.next
            length += 1
        return length

    def insert_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                # go to next node till we get last node (node.next = None)
                last_node = last_node.next

            # append new node at end
            last_node.next = new_node

    def insert_first(self, new_node):
        if self.head is None:
            self.head = new_node
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node
        del temp_node

        '''
        #or
        new_node.next = self.head
        self.head = new_node
        '''

    def insert_at(self, new_node, pos):
        if pos < 0 or pos > self.list_length():
            print("Invalid position")
            return

        if pos == 0:
            self.insert_first(new_node)
            return

        curr_pos = 0
        curr_node = self.head
        while True:
            prev_node = curr_node
            curr_node = curr_node.next
            curr_pos += 1

            if curr_pos == pos:
                prev_node.next = new_node
                new_node.next = curr_node
                break

    def delete_end(self):
        curr_node = self.head
        while curr_node.next is not None:
            prev_node = curr_node
            curr_node = curr_node.next

        prev_node.next = None

    def delete_first(self):
        if not self.is_list_empty():
            prev_head = self.head
            self.head = self.head.next
            prev_head.next = None
        else:
            print("Linked List is empty! Can't delete")

    def delete_at(self, pos):
        if pos < 0 or pos >= self.list_length():
            print("Cannot delete! ")
            return

        if not self.is_list_empty():
            if pos == 0:
                self.delete_first()
                return
            curr_pos = 0
            curr_node = self.head
            while True:
                prev_node = curr_node
                curr_node = curr_node.next
                curr_pos += 1

                if curr_pos == pos:
                    prev_node.next = curr_node.next
                    curr_node.next = None
                    break

    def print_list(self):
        if self.head is None:
            print("List is empty!")
            return
        while True:
            if self.head is None:
                break
            print(self.head.data)
            self.head = self.head.next

    def display(self):
        if self.head is None:
            print("List is empty!")
            return
        elements = []
        while self.head is not None:
            elements.append(self.head.data)
            self.head = self.head.next
        print(elements)


# l = ['a', 'b', 'c', 'd']
l = [1, 3, 7, 9, 10]
linked_list = LinkedList()

for name in l:
    node = Node(name)
    linked_list.insert_end(node)
    # linked_list.insert_first(Node(0))

linked_list.insert_at(Node(8), 3)
linked_list.delete_end()
# linked_list.print_list()
# linked_list.display()
