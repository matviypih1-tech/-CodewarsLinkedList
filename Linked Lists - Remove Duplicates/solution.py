class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    seen = set()
    cur = head
    prev = None

    while cur:
        if cur.data in seen:
            prev.next = cur.next
        else:
            seen.add(cur.data)
            prev = cur
        cur = cur.next

    return head
