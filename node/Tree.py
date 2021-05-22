from node.Node import Node

"""
A simple visualiser for current graph structure
"""
DOUBLE = "├──"
SINGLE = "└──"
BAR = "│"
INDENT = "\t"


class Tree:
    def __init__(self, root: Node):
        self.root = root

    def _print_bar(self, bar_level):
        for i in range(1, len(bar_level)):
            print(BAR + (bar_level[i] - bar_level[i - 1]) * INDENT, end="")

    def _render(self, node, level, bar_level=None):
        if bar_level is None:
            bar_level = [0]

        print(node.id)
        children = node.children

        for i in range(len(children)):
            self._print_bar(bar_level)

            print(INDENT * (level - bar_level[-1]), end="")

            if i != len(children) - 1:
                if not children[i].children:
                    print(DOUBLE, end=" ")
                else:
                    print(SINGLE, end=" ")

                # register bar level for children
                # warning: do not use bar_level, or else all recursive calls will use the same object
                new_bar_level = bar_level + [level + 1]

            else:
                print(SINGLE, end=" ")

                new_bar_level = bar_level.copy()

            self._render(children[i], level + 1, new_bar_level)

    def render(self):
        self._render(self.root, 0)


if __name__ == '__main__':
    print("Root")
    print(DOUBLE + " sub1")
    print(SINGLE + " sub2")
