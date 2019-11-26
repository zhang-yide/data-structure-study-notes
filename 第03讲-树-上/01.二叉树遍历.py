from binary_tree import root


def pre_traverse(root):
    """先序遍历"""
    if root:
        print(root.value)
        pre_traverse(root.left)
        pre_traverse(root.right)


def mid_traverse(root):
    """中序遍历"""
    if root:
        mid_traverse(root.left)
        print(root.value)
        mid_traverse(root.right)


def after_traverse(root):
    """后序遍历"""
    if root:
        after_traverse(root.left)
        after_traverse(root.right)
        print(root.value)


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


if __name__ == '__main__':
    print('先序遍历:')
    pre_traverse(root)
    print('中序遍历:')
    mid_traverse(root)
    print('后序遍历:')
    after_traverse(root)
    print('层序遍历')
    level_traverse(root)
