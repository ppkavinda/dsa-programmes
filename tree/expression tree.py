# expression tree


# implementing the liner Queue class for store the expression
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]

    def printQ(self):
        print(self.items)
# end implementing the queue


class Node:
    def __init__(self, data_in):
        self.data = data_in
        self.left = None
        self.right = None


class expression_tree:
    def __init__(self, exp):
        exp_q = Queue()
        for character in exp:
            exp_q.enqueue(character)

        self.root = Node(None)
        self._build_expression_tree(self.root, exp_q)

    # function for build the expression tree automatically, recursively
    def _build_expression_tree(self, current_node, exp_q):
        token = exp_q.dequeue()
        if token == "(":
            current_node.left = Node(None)
            self._build_expression_tree(current_node.left, exp_q)

            current_node.data = exp_q.dequeue()
            current_node.right = Node(None)
            self._build_expression_tree(current_node.right, exp_q)

            exp_q.dequeue()
        else:
            current_node.data = int(token)

# convert the expression tree to a string
    def exp_to_string(self, current_node):
        if current_node.left is None and current_node.right is None:
            return str(current_node.data)
        else:
            exp_str = "("
            exp_str += self.exp_to_string(current_node.left)
            exp_str += str(current_node.data)
            exp_str += self.exp_to_string(current_node.right)
            exp_str += ")"

            return exp_str

# traversals
    def post_order(self):
        if self.root.left is not None:
            self._post_order(self.root)

    # helper function for post_order
    def _post_order(self, current_node):
        if current_node.left is not None:
            self._post_order(current_node.left)

        if current_node.right is not None:
            self._post_order(current_node.right)
        print(current_node.data, end='')

    def breadth_first(self):
        q = Queue()
        q.enqueue(self.root)

        while not q.isEmpty():
            node = q.dequeue()
            print(node.data)

            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)

ex = expression_tree("((((4+5)*3)/((8-7)+2))-((5*(7-5))-8))")
ex.post_order()
print()

