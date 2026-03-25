from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def get_nth(node, index):
    current = node
    i = 0
    while current is not None:
        if i == index:
            return current
        current = current.next
        i+=1
    raise Exception("Index out of range")
