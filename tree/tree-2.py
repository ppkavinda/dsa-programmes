class Tree:    def __init__(self, data):        self.left = None        self.right = None        self.data = data    def insert_left(self, data, place):        new_node = Tree(data)        if self.left is None:            self.left = new_node        elif self.left.data == place:            if self.left is None:                self.left = new_node                return            else:                self.left.insert_left(data, place)                self.right.insert_left(data, place)        else:            print("Cannot find the root: " + str(place) + ".")    def insert_right(self, data, place):        new_node = Tree(data)        if self.right is None:            self.right = new_node        elif self.right.data == place:            if self.right is None:                self.right = new_node                return            else:                self.left.insert_right(data, place)                self.right.insert_right(data, place)        else:            print("Cannot fine the root: " + str(place) + ".")    def pre_order(self):        print(self.data)        if self.left:            self.left.pre_order()        if self.right:            self.right.pre_order()    def in_order(self):        if self.left:            self.left.in_order()        print(self.data)        if self.right:            self.right.in_order()    def post_order(self):        if self.left:            self.left.post_order()        if self.right:            self.right.post_order()        print(self.data)t = Tree("a")t.insert_left("b", "a")t.insert_right("c", "a")t.insert_right("d", "b")# t.insert_left("e", "c")# t.insert_left("f", "e")print("\npre")t.pre_order()print("\nin")t.in_order()print("\npost")t.post_order()