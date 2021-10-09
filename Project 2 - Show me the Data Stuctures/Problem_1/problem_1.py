class DoublyNode:
    def __init__(self, value=None):
        self.next = None
        self.prev = None
        self.value = value

    def __repr__(self):
        return str(self.value)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, value):
        """
            Add's value at starting of the list.
        """
        if not self.head:
            self.head = DoublyNode(value)
            self.tail = self.head
        else:
            h_node = DoublyNode(value)
            h_node.next = self.head
            self.head.prev = h_node
            self.head = h_node
        self.length += 1

        return self.head

    def append(self, value):
        """
            Add's value at list tail.
        """
        if self.length == 0:
            self.head = DoublyNode(value)
            self.tail = self.head
        else:
            t_node = DoublyNode(value)
            t_node.prev = self.tail
            self.tail.next = t_node
            self.tail = t_node
        self.length += 1

        return self.tail

    def search(self, value):
        """
            Search for the value accross the linked list
        """
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next

    def remove(self, value):
        """
            Remove the node from list, which first matches the node.
        """
        node = self.head
        while node:
            if node.value == value:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.length -= 1
                return node
            node = node.next

    def size(self):
        """
            Return size of linked list
        """
        return self.length

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail


class LRU_Cache(DoublyLinkedList):

    def __init__(self, capacity):
        # Initialize class variables
        super().__init__()
        self.max_size = capacity
        self.storage = dict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        node = self.storage.get(key, -1)

        if node != -1:
            self.__move_node_to_tail(node)
            self.storage[key] = self.get_tail()
            self.storage[key].key = key
            return self.storage[key].value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.
        if key not in self.storage:
            if not self.size() < self.max_size:
                storage_key = self.get_head().key
                del self.storage[storage_key]
                self.__remove_head_node()
            self.storage[key] = self.append(value)
            self.storage[key].key = key

    def __move_node_to_tail(self, node):
        """
            Move the given node to end of linked list(tail).
        """
        value = node.value

        if node.prev:
            node.prev.next = node.next
        elif self.size() > 1:
            # if this is head node
            self.head = node.next
            self.head.prev = None

        if node.next:
            node.next.prev = node.prev
        elif self.size() > 1:
            # if this is tail node
            self.tail = self.tail.prev
            self.tail.next = None

        if self.size() > 1:
            self.length -= 1
            self.append(value)

    def __remove_head_node(self):
        """
            Removes the head node i.e least recently used item.
        """
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
