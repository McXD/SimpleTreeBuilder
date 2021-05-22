from client.Command import parse


class View:
    """
    Command Line Interface
    """

    def put(self, output):
        """
        Output to user
        """
        print(output)

    def get(self, prompt):
        inputs = input(prompt)
        return parse(inputs), inputs
