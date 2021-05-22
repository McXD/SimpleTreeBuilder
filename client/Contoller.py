from client.Model import Model
from client.View import View
from client.Command import Command
from node.Tree import Tree
from client.exceptions import MalformedCommandException
from node import Graph
import os

PROMPT_SYMBOL = "$"

class Controller:
    def __init__(self, model=None, view=None):
        if not model:
            self.model = Model()
        if not view:
            self.view = View()

    def run(self):
        while True:
            try:
                id = ""
                if self.model.currentNode:
                    id = self.model.currentNode.id

                command, args= self.view.get(PROMPT_SYMBOL + " " + id + ": ")
                arg = command.parse(args)

                if command == Command.INIT:
                    if len(arg) == 1:
                        self.model.init(arg[0])
                    elif len(arg) == 2:
                        self.model.init(arg[0], label=arg[1])

                elif command == Command.TOUCH:
                    if not self.model.currentNode:
                        raise MalformedCommandException("Error: No parent found. Use init command to initialise a tree.")
                    if len(arg) == 1:
                        self.model.newNode(arg[0])
                    elif len(arg) == 2:
                        self.model.newNode(arg[0], label=arg[1])
                    elif len(arg) == 3:
                        self.model.newNode(arg[0], label=arg[1], eLabel=arg[2])

                elif command == Command.CD:
                    self.model.cd(arg[0])

                elif command == Command.LABEL:
                    if len(arg) == 0:
                        self.view.put(self.model.currentNode.label)
                    else:
                        self.model.label(" ".join(arg))

                elif command == Command.CR:
                    self.model.switch(arg[0])

                elif command == Command.TREE:
                    Tree(self.model.currentNode).render()

                elif command == Command.ELABEL:
                    if len(arg) == 0:
                        self.view.put(self.model.currentNode.eLabel)
                    else:
                        self.model.elabel(" ".join(arg))

                elif command == Command.EXPORT:
                    Graph.OUTDIR = os.getcwd()
                    Graph.OUTNAME = "out"

                    if len(arg) == 0:
                        Graph.Graph(self.model.currentRoot).render()
                    elif len(arg) == 1:
                        Graph.Graph(self.model.currentRoot, title=arg[0]).render()
                    elif len(arg) == 2:
                        Graph.Graph(self.model.currentRoot, title=arg[0]).render(filename=arg[1])
                    elif len(arg) == 3:
                        Graph.Graph(self.model.currentRoot, title=arg[0]).render(filename=arg[1], directory=arg[2])
                    elif len(arg) == 4:
                        Graph.OUTNAME = arg[1]
                        Graph.OUTDIR = arg[2]
                        Graph.Graph(self.model.currentRoot, title=arg[0], format=arg[3]).render()
                    else:
                        raise MalformedCommandException("Cannot render")

            except Exception as e:
                self.view.put(str(e))