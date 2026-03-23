from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr is 'null':
        return None
    values = list_repr.split(" -> ")[:-1]
    head = None
    for i in values[::-1]:
        head = Node(int(i) , head)
    return head
