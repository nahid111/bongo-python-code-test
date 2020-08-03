class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None


def lca(node1, node2):
    if type(node1) is not Node or type(node2) is not Node:
        return None

    # Check if any of two nodes is root
    if node1.parent is None:
        return node1.value
    if node2.parent is None:
        return node2.value

    # Check if one node's value is equal to another node's parent's value
    if node1.value == node2.parent.value:
        return node1.value
    if node2.value == node1.parent.value:
        return node2.value

    # check if one node is smaller than another node's parent
    if node1.value < node2.parent.value:
        return lca(node1, node2.parent)
    elif node2.value < node1.parent.value:
        return lca(node2, node1.parent)

    # check if common parent exists
    if node1.parent.value == node2.parent.value:
        return node1.parent.value

    return lca(node1.parent, node2.parent)


