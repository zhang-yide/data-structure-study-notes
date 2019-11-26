from binary_tree import root


def binary_tree_max(root):
    """最大元素"""
    if not root:
        return None
    elif not root.right:
        return root
    else:
        return binary_tree_max(root.right)


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


def binary_tree_delete(root, n):
    """
    二叉树删除：
    如果该结点为叶，则直接删除该结点，并置父结点指针为None
    如果该结点有一侧数据，则将该结点替换为其子结点
    如果该结点有两侧数据，则将该结点的值替换为其左侧最大结点的值，并删除该最大结点
    """
    if not root:
        print("没有找到要删除的元素")
    elif n > root.value:
        root.right = binary_tree_delete(root.right, n)
    elif n < root.value:
        root.left = binary_tree_delete(root.left, n)
    else:  # 找到该结点
        if root.left and root.right:  # 有两侧数据
            tmp = binary_tree_max(root.left)  # 找到左侧最大结点
            root.value = tmp.value  # 将该结点的值替换为其左侧最大结点的值
            root.left = binary_tree_delete(root.left, tmp.value)  # 删除左侧最大结点
        elif not root.left:  # 如果左侧为空
            root = root.right  # 将该结点替换为其子结点
        elif not root.right:  # 如果右侧为空
            root = root.left
    return root


if __name__ == '__main__':
    n = 10
    binary_tree_delete(root, n)
    level_traverse(root)
