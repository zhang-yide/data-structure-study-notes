from binary_tree import root, BinaryTree


def level_traverse(root):
    """层序遍历"""
    queue = []
    queue.append(root)
    while queue:
        T = queue.pop()  # 结点出队
        print(T.value)
        # 访问结点左右孩子
        if T.left:
            queue.insert(0, T.left)  # 左右孩子入队
        if T.right:
            queue.insert(0, T.right)


def binary_tree_insert(root, n):
    """二叉树插入"""
    if not root:
        # 如果为空，则返回一个结点的二叉树
        root = BinaryTree(n)
    else:
        if n > root.value:
            root.right = binary_tree_insert(root.right, n)
        elif n < root.value:
            root.left = binary_tree_insert(root.left, n)
    return root


if __name__ == '__main__':
    n = 19
    binary_tree_insert(root, n)
    level_traverse(root)
