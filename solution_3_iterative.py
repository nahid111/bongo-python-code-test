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
    elif node2.parent is None:
        return node2.value

    visited = {
        node1.value: node1.parent.value
    }

    # visit each parent of node1 till root
    current = node1
    while True:
        parent = current.parent if current.parent else None
        if not parent:
            break
        if parent.value not in visited:
            visited[parent.value] = parent.parent.value if parent.parent else None
        current = parent

    # visit each parent of node2 until LCA is found
    current = node2
    while True:
        if current.value in visited:
            return current.value
        elif not current.parent:
            return current.value
        elif current.parent.value in visited:
            return current.parent.value
        current = current.parent

