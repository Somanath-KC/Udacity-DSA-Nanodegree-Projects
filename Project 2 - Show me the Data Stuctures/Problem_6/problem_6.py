class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string[:-4]

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_set(self):
        output_set = set()

        if self.size() == 0:
            return output_set

        node = self.head
        while node:
            output_set.add(node.value)
            node = node.next

        return output_set


def union(llist_1, llist_2):
    # Your Solution Here
    set_1 = llist_1.to_set()
    set_2 = llist_2.to_set()

    union_set = set_1.union(set_2)
    union_list = LinkedList()

    for i in union_set:
        union_list.append(i)

    return union_list


def intersection(llist_1, llist_2):
    # Your Solution Here
    set_1 = llist_1.to_set()
    set_2 = llist_2.to_set()

    intersec_set = set_1.intersection(set_2)
    intersec_list = LinkedList()

    for i in intersec_set:
        intersec_list.append(i)

    return intersec_list


#####     #####
#   Testing   #
#####     #####

# Test case 1
print("\n",  "#"*10, " - Test Case 1 - ", "#"*10, "\n")

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2
print("\n",  "#"*10, " - Test Case 2 - ", "#"*10, "\n")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 3]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))


# Test case 3 / One Empty List
print("\n",  "#"*10, " - Test Case 3 - ", "#"*10, "\n")

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_5 = []
element_6 = [1, 7, 8, 9, 11, 21, 1]

for i in element_5:
    linked_list_5.append(i)

for i in element_6:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
print(intersection(linked_list_5, linked_list_6))  # Return's None

# Passing two empty lists / Returns None for both
print(union(linked_list_5, linked_list_5))
print(intersection(linked_list_5, linked_list_5))
