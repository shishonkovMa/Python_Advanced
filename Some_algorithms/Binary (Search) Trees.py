import math


class Node:
    def __init__(self, key=0, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent


def tree_size(root):
    if root is None:
        return 0
    return 1 + tree_size(root.left) + tree_size(root.right)


def tree_max(T):
    if T is None:
        return -math.inf
    a = max(tree_max(T.left), tree_max(T.right))
    if a < T.key:
        return T.key
    else:
        return a


def _check_BST(root):
    if root is None:
        return True, None, None
    _left = _check_BST(root.left)
    _right = _check_BST(root.right)
    if _right[1] is None:
        _right = (True, root.key, root.key)
    if _left[1] is None:
        _left = (True, root.key, root.key)
    if (_left[1] <= root.key
            and _left[2] <= root.key
            and _right[1] >= root.key
            and _right[2] >= root.key):
        bst = True
    else:
        bst = False
    maxima = _right[1]
    minima = _left[2]
    return bst, maxima, minima


def check_BST(root):
    return _check_BST(root)[0]


def _min_diff(root):
    if root is None:
        return math.inf, math.inf, -math.inf
    res_right = _min_diff(root.right)
    res_left = _min_diff(root.left)
    min_val = min(root.key, res_left[1])
    max_val = max(root.key, res_right[2])
    min_diff = min(abs(res_left[2] - res_right[1]),
                   abs(root.key - res_left[2]),
                   abs(root.key - res_right[1]),
                   abs(res_left[0]),
                   abs(res_right[0]))
    return min_diff, min_val, max_val


def min_diff(root):
    return _min_diff(root)[0]


def _count_distinct(root, container=set()):
    if root is None:
        return 0, None
    _left = _count_distinct(root.left, container)
    _right = _count_distinct(root.right, container)
    container.add(_left[0])
    container.add(_right[0])
    container.add(root.key)
    return root.key, container


def count_distinct(root):
    if _count_distinct(root) == 0:
        return 0
    return len(_count_distinct(root)[1]) - 1


#Тесты
# if __name__ == "__main__":
#     T = Node(3)
#     insert(T, Node(1))
#     insert(T, Node(2))
#     # should print True
#     print(check_BST(T))
#     # should print 1
#     print(min_diff(T))
