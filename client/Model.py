from node.Node import Node
from client.exceptions import MalformedCommandException


class Model:
    def __init__(self):
        self.roots = []
        self.currentRoot = None
        self.currentNode = None

    def init(self, id, label=""):
        node = Node(id, label=label)
        self.roots.append(node)
        self.currentNode = node
        self.currentRoot = node

    def switch(self, root):
        """
        Root is referenced by their index in model.roots
        """
        try:
            self.currentRoot = self.roots[root]
            self.currentNode = self.currentRoot
        except IndexError:
            raise MalformedCommandException("Index not found.")

    def label(self, newLabel):
        self.currentNode.label = newLabel

    def elabel(self, newLabel):
        self.currentNode.eLabel = newLabel

    def newNode(self, id, label="", eLabel=""):
        Node(id, label, parent=self.currentNode, eLabel=eLabel)

    def cd(self, child):
        """
        Child node is referenced by number, that is, their index in parent.children
        """
        try:
            if child >=0:
                self.currentNode = self.currentNode.children[child]
            else:
                self.currentNode = self.currentNode.parent
        except IndexError:
            raise MalformedCommandException("Index not found.")