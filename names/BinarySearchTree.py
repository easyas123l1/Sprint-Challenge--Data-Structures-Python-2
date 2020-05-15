class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        searching = True
        current = self
        # searching for valid spot
        while searching:
            # test if value is smaller
            if value < current.value:
                # if smaller and No value insert node
                if current.left == None:
                    current.left = BinarySearchTree(value)
                    searching = False
                # if smaller and left node has value go left
                else:
                    current = current.left
            # value is >= move right
            else:
                # if no value right insert node
                if current.right == None:
                    current.right = BinarySearchTree(value)
                    searching = False
                # if larger and right node has value go right
                else:
                    current = current.right

        # Return True if the tree contains the value
        # False if it does not
    def contains(self, target):
        # when we start, self will be the root
        # compare the target against self
        if target == self.value:
            return True
        # if target > self.value go right else go left
        if target > self.value:
            if not self.right:
                return False
            # go right
            return self.right.contains(target)
        else:
            if not self.left:
                return False
            # go left
            return self.left.contains(target)
