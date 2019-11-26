from binary_tree import root


def print_leaves(root):
    """打印树叶"""
    if root:
        if not root.left and not root.right:
            print(root.value)
        print_leaves(root.left)
        print_leaves(root.right)


if __name__ == '__main__':
    print_leaves(root)
