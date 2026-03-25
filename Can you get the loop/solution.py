def loop_size(node):
    slow = node
    fast = node
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    loop_len = 1
    current = slow.next
    while current != slow:
        loop_len += 1
        current = current.next

    return loop_len
