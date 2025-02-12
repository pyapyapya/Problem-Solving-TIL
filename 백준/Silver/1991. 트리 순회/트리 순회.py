from typing import Dict

class Node:
    __slots__ = ("root", "left_child", "right_child")
    def __init__(self, root, left_child = ".", right_child = "."):
        self.root: str = root
        self.left_child: str = left_child
        self.right_child: str = right_child
    
    def __str__(self):
        return self.root + " " + self.left_child + " " + self.right_child

class Tree:
    def __init__(self):
        self.tree: Dict[str, Node] = {}
        self.tree["."] = Node(".")
    
    def __getitem__(self, root):
        return self.tree.get(root)
    
    def __setitem__(self, root: str, node: Node):
        self.tree[root] = node



def pre_order(tree: Tree, root: str):
    node = tree[root]
    if root == ".":
        return
    print(root, end="")
    pre_order(tree, node.left_child)
    pre_order(tree, node.right_child)


def in_order(tree: Tree, root: str):
    node = tree[root]
    if root == ".":
        return
    in_order(tree, node.left_child)
    print(root, end="")
    in_order(tree, node.right_child)

def post_order(tree: Tree, root: str):
    node = tree[root]
    if root == ".":
        return
    post_order(tree, node.left_child)
    post_order(tree, node.right_child)
    print(root, end="")


tree = Tree()
n = int(input())
for _ in range(n):
    root, left, right = input().split(" ")
    node = Node(root, left, right)
    tree[root] = node

pre_order(tree, "A")
print()
in_order(tree, "A")
print()
post_order(tree, "A")