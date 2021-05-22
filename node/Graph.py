from graphviz import Digraph

OUTDIR = "/Users/fengyunlin/Documents"
OUTNAME = "out"

"""
A wrapper on graphviz.Digraph
"""
class Graph:
    def __init__(self, root, title=None, format='png'):
        self.root = root
        self.graph = Digraph(title, format=format)
        self.map = dict() # keep object-name mapping

    def _name(self, node):
        return str(hash(node))

    def _register(self, node):
        child_name = self._name(node)
        self.graph.node(child_name, label=str(node.id + "\n" + node.label))
        self.map[node] = child_name

        if node.parent:
            self.graph.edge(self.map[node.parent], child_name, label=node.eLabel)

    def _build(self, node):
        self._register(node)
        for i in node.children:
            self._build(i)

    def render(self, filename=OUTNAME, directory=OUTDIR):
        self._build(self.root)
        self.graph.render(filename=filename, directory=directory)
