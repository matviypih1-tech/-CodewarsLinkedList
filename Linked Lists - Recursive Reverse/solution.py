class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    prev = None
    cur =  head
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev
