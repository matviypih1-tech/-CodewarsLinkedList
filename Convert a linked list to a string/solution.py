def stringify(node):
    res = ''
    current = node
    while current is not None:
        res += str(current.data) + ' -> '
        current = current.next
    res += 'None'
    return res
