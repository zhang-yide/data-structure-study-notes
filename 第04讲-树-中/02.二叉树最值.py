from binary_tree import root


def binary_tree_min(root):
    """最小元素"""
    if not root:
        return None
    elif not root.left:
        return root
    else:
        return binary_tree_min(root.left)


def binary_tree_max(root):
    """最大元素"""
    if not root:
        return None
    elif not root.right:
        return root
    else:
        return binary_tree_max(root.right)


if __name__ == '__main__':
    print(binary_tree_min(root).value)
    print(binary_tree_max(root).value)
