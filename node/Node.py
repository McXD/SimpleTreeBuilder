"""
Core class.
Node provides graphviz node creation and edge establishment interface.
A node can only have one parent, zero or more children.
"""


class Node:
    def __init__(self, id, label="", parent=None, eLabel=""):
        self.id = id
        self.label = label
        self.parent = parent
        self.children = []  # keep a list of children for easy tracking
        self.eLabel = eLabel

        # add self to parent's children list
        if parent:
            self.parent.addChild(self)

    """
    Build an edge between self and parent, with an optional label
    """
    def connect(self, parent, eLabel=None):
        self.parent = parent
        self.eLabel = eLabel
        self.parent.addChild(self)

    def addChild(self, child):
        self.children.append(child)


if __name__ == '__main__':
    root = Node('one',1)
    two = Node('two', 2, root)
    three = Node('three', 3, root)
    four = Node('four', 4, two)
    five = Node('five', 5, two)
    six = Node('six', 6, three)
    seven = Node('seven', 7, three)

    from Tree import Tree

    tree = Tree(root)
    tree.render()

    from Graph import Graph

    graph = Graph(root)
    graph.render()
