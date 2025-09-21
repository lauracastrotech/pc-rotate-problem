# DO NOT MODIFY THE NODE CLASS
class Node:
    def __init__(self, value, next=None):
        self.value = value 
        # if next is None, this is the last element in the list
        self.next = next

    def __eq__(self, other):
        '''
        Understanding this function is NOT necessary for solving the problem;
        it is only used for the assertions.
        Feel free to explore your curiosity of how this works after the interview :)
        '''
        try:
            return (type(other) == Node and 
                    self.value == other.value and 
                    self.next == other.next)
        except RecursionError:
            raise Exception("Linked list has a cycle or is too large")


def rotate(head, k):
    # empty list or a single node
    if not head or not head.next:
        return head

    # Find the length of the linked list
    length = 1
    current = head
    while current.next:
        length += 1
        current = current.next
    
    # No need to rotate if k is 0 or a multiple of the list length
    k = k % length
    if k == 0:
        return head  
    
    # Find the new tail and new head
    current.next = head  # Connect the tail to the head to form a circular list
    new_tail_pos = length - k - 1
    new_tail = head
    for _ in range(new_tail_pos):
        new_tail = new_tail.next
    
    # Update the new head 
    new_head = new_tail.next
    new_tail.next = None
    
    return new_head




# Input list: a->b->c->d->e
# Rotate by 1
# Output list: e->a->b->c->d
list_1 = Node('a', Node('b', Node('c', Node('d', Node('e')))))
expected = Node('e', Node('a', Node('b', Node('c', Node('d')))))
assert rotate(list_1, 1) == expected

# Input list: a->b->c->d->e
# Rotate by 2
# Output list: d->e->a->b->c
list_2 = Node('a', Node('b', Node('c', Node('d', Node('e')))))
expected = Node('d', Node('e', Node('a', Node('b', Node('c')))))
assert rotate(list_2, 2) == expected

# Input list: a->b->c->d->e
# Rotate by 10
# Input list: a->b->c->d->e
list_3 = Node('a', Node('b', Node('c', Node('d', Node('e')))))
expected = Node('a', Node('b', Node('c', Node('d', Node('e')))))
assert rotate(list_3, 10) == expected

# Input list: 55->8->2->99
# Rotate by 6
# Output list: 2->99->55->8
list_4 = Node(55, Node(8, Node(2, Node(99))))
expected = Node(2, Node(99, Node(55, Node(8))))
assert rotate(list_4, 6) == expected

# Input list: 1->2
# Rotate by 5
# Output list: 2->1
list_5 = Node(1, Node(2))
expected = Node(2, Node(1))
assert rotate(list_5, 5) == expected

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
