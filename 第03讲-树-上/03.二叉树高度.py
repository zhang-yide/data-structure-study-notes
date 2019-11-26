from binary_tree import root


def get_height(root):
    """
    打印高度
    height = max(height_left, height_right) + 1
    """
    max_height = 0
    if root:
        height_left = get_height(root.left)
        height_right = get_height(root.right)
        max_height = max(height_left, height_right)
        return max_height + 1
    else:
        return 0


if __name__ == '__main__':
    print(get_height(root))
