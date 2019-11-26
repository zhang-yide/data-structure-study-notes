class BinaryTree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = BinaryTree(18,
                  left=BinaryTree(10,
                                  left=BinaryTree(7,
                                                  right=BinaryTree(9)
                                                  ),
                                  right=BinaryTree(15)
                                  ),
                  right=BinaryTree(20,
                                   right=BinaryTree(22)
                                   )
                  )
