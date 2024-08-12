class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insertion at the start
    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Insertion at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    # Insertion at the middle
    def insert_at_middle(self, data, position):
        if position <= 0:
            print("Invalid position! Position should be >= 1.")
            return

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            for _ in range(position - 1):
                if temp.next is None:
                    break
                temp = temp.next

            new_node.next = temp.next
            new_node.prev = temp

            if temp.next:
                temp.next.prev = new_node

            temp.next = new_node

    # Method to print the list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> " if temp.next else "\n")
            temp = temp.next

# Example Usage
dll = DoublyLinkedList()
dll.insert_at_start(10)
dll.insert_at_end(20)
dll.insert_at_start(5)
dll.insert_at_middle(15, 2)  # Position is based on 1-indexing
dll.insert_at_end(25)
dll.print_list()
