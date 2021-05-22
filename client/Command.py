from enum import Enum, auto
from client.exceptions import MalformedCommandException


def parse(args):
    args = args.split()

    c = args[0]
    if c == 'init':
        return Command.INIT
    elif c == 'touch':
        return Command.TOUCH
    elif c == 'cd':
        return Command.CD
    elif c == 'cr':
        return Command.CR
    elif c == 'label':
        return Command.LABEL
    elif c == 'tree':
        return Command.TREE
    elif c == 'elabel':
        return Command.ELABEL
    elif c == 'export':
        return Command.EXPORT
    else:
        raise MalformedCommandException("Error: Command not found: " + c)


class Command(Enum):
    INIT = auto()  # initialize a tree
    TOUCH = auto()  # touch a node
    CD = auto()  # navigate through nodes
    CR = auto()  # change root
    LABEL = auto()  # edit contents of a node
    ELABEL = auto()  # edit the edge label
    TREE = auto()  # listing
    EXPORT = auto()  # export

    def __init__(self, args):
        self.args = args

    def parse(self, args):
        if self == Command.INIT:
            return self._init(args)
        elif self == Command.TOUCH:
            return self._touch(args)
        elif self == Command.CD:
            return self._cd(args)
        elif self == Command.CR:
            return self._cr(args)
        elif self == Command.LABEL:
            return self._label(args)
        elif self == Command.TREE:
            return self._tree(args)
        elif self == Command.ELABEL:
            return self._elabel(args)
        elif self == Command.EXPORT:
            return self._export(args)

    def _init(self, args):
        """
        Usage: init label
        """
        args = args.split()
        if len(args) not in [1,2]:
            raise MalformedCommandException("Usage: init <id> [<label>]")

        return args[1:]

    def _touch(self, args):
        """
        Usage: touch <label>
        """
        args = args.split()
        if len(args) not in [2, 3, 4]:
            raise MalformedCommandException("Usage: touch <id> [<label> <eLabel>]")

        return args[1:]

    def _cd(self, args):
        """
        Usage: cd <node>
        """
        args = args.split()
        if len(args) != 2:
            raise MalformedCommandException("Usage: cd <node_index>")

        try:
            int(args[1])
        except:
            raise MalformedCommandException("Use the index to reference node.")

        return [int(args[1])]

    def _cr(self, args):
        """
        Usage: cd <node>
        """
        args = args.split()
        if len(args) != 2:
            raise MalformedCommandException("Usage: cr <root_index>")

        try:
            int(args[1])
        except:
            raise MalformedCommandException("Use the index to reference node.")

        return [int(args[1])]

    def _label(self, args):
        """
        Usage: label [<label>]
        """

        args = args.split()

        return args[1:]

    def _tree(self, args):
        """
        Usage: tree
        """

        args = args.split()
        if len(args) != 1:
            raise MalformedCommandException("Usage: tree")

        return list()

    def _elabel(self, args):
        """
        Usage: elabel [<label>]
        """

        args = args.split()

        return args[1:]

    def _export(self, args):
        """
        Usage: export [<title> <filename> <directory> <format>]
        """

        args = args.split()

        if len(args) > 5:
            raise MalformedCommandException("Usage: export [<title> <filename> <directory> <format>]")

        return args[1:]
