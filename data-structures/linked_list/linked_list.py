# emre.me/data-structures/linked-lists/
class Node:
    def __init__(self, data):
        """
        A node in singly linked list
        :param data:
        """
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        """
        create new (empty) singly linked list: O(1)
        - For flexible implementation: use head, tail, size
        """
        self.head = None
        self.tail = None
        self.size = 0

    def prepend(self, data):
        """
        Insert a new node at the beginning of LL.
        - O(1)
        :param data:
        :return:
        """
        # If head is already present
        if self.head:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = Node(data)
            self.tail = self.head
        self.size += 1

    def append(self, data):
        """
        - O(1), as we are using tail pointer
        :param data:
        :return:
        """
        if self.head:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = Node(data)
            self.tail = self.head
        self.size += 1

    def get(self, index):
        """
        Get the nth-index node. If node not found, then return None
        :param index:
        :return:
        """
        if not (0 <= index < self.size and self.head):
            return None

        if not self.head:
            return None

        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.data

    def add_at_index(self, index, data):
        """

        :param index:
        :param data:
        :return:
        """
        if not (0 <= index < self.size):
            return print(f'index {index} is out of limit')
        elif index == self.size:
            self.append(data)
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            new_node = Node(data)
            new_node.next = curr.next
            curr.next = new_node
        self.size += 1

    def delete_at_index(self, index):
        """

        :param index:
        :return:
        """
        if not (0 <= index < self.size):
            return print(f'index {index} is out of range')
        elif index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            if curr.next.next is None:
                curr.next = None
                self.tail = curr
            else:
                curr.next = curr.next.next

        self.size += 1

# l = ['a', 'b', 'c', 'd']
l = [1, 3, 7, 9, 10]
linked_list = LinkedList()

for name in l:
    node = Node(name)
    linked_list.append(node.data)
    # linked_list.insert_first(Node(0))

linked_list.add_at_index(3, Node(8).data)
linked_list.delete_at_index(4)
# linked_list.print_list()
# linked_list.display()
