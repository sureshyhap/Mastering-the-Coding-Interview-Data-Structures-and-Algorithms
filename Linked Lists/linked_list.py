class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.size = 1

    def prepend(self, data):
        self.head = Node(data, self.head)
        self.size += 1

    def append(self, data):
        self.tail.next = Node(data)
        self.tail = self.tail.next
        self.size += 1

    def lookup(self, data):
        present_node = self.head
        while present_node and present_node.data != data:
            present_node = present_node.next
        if not present_node:
            return None
        return present_node

    def insert(self, after_this_data, data):
        """Assumes not inserting before head or after tail."""
        present_node = self.head
        while present_node and present_node.data != after_this_data:
            present_node = present_node.next
        if not present_node:
            return
        present_node.next = Node(data, present_node.next)
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            return
        self.head = self.head.next
        # There was just one element so head and tail both become None
        if not self.head:
            self.tail = None
        self.size -= 1

        #####################
    def delete(self, after_this_data):
        if self.size == 0:
            return
        if after_this_data == self.head.data:
            self.head = self.head.next
            return
        present_node = self.head
        while present_node and present_node.next.data != after_this_data:
            present_node = present_node.next
        if not present_node:
            return
        self.size -= 1
        #####################

    def __str__(self):
        s = ""
        present_node = self.head
        while present_node:
            s += str(present_node.data) + " "
            present_node = present_node.next
        return s
            

ll = Linked_List(5)
ll.prepend(10)
ll.append(20)
ll.append(300)
ll.insert(20, 50)
ll.pop_front()

print(ll)
