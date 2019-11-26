class BinaryTree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = BinaryTree('A',
                  left=BinaryTree('B',
                                  left=BinaryTree('D'),
                                  right=BinaryTree('F',
                                                   left=BinaryTree('E')
                                                   )
                                  ),
                  right=BinaryTree('C',
                                   left=BinaryTree('G',
                                                   right=BinaryTree('H')
                                                   ),
                                   right=BinaryTree('I')
                                   )
                  )
