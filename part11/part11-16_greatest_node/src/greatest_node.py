# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: Node):
    greatest = root.value

    if root.left_child is not None:
        left = greatest_node(root.left_child)
        if left > greatest:
            greatest = left
            
    if root.right_child is not None:
        right = greatest_node(root.right_child)
        if right > greatest:
            greatest = right

    return greatest