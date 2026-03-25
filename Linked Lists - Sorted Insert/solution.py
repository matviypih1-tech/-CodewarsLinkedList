""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    current = head
    while current is not None:
        if current > current.next:
            data = data.next
            data.next = data
    return data
