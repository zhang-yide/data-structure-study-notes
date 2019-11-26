from binary_tree import root


def binary_tree_search(root, n):
    while(root):
        if n > root.value:
            root = root.right
        elif n < root.value:
            root = root.left
        else:
            return root
    return None


if __name__ == '__main__':
    n = 9
    print(binary_tree_search(root, n))
