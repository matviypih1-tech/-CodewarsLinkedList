class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if not head or not head.next:
        raise ValueError("List must have at least two nodes")
    first_head = first_tail = None
    second_head = second_tail = None
    current = head
    toggle = True
    while current:
        next_node = current.next
        current.next = None
        if toggle:
            if not first_head:
                first_head = first_tail = current
            else:
                first_tail.next = current
                first_tail = current
        else:
            if not second_head:
                second_head = second_tail = current
            else:
                second_tail.next = current
                second_tail = current
        toggle = not toggle
        current = next_node
    return Context(first_head, second_head)
