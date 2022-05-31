# Given a binary tree root, check if its symmetric around its center (a mirror of itself)

# Initial thoughts: Break down tree into just root nodes, check reflection on og root
#                   Like, actual leaf nodes from left to right are indexed ascending when left of root, and
#                   leaf nodes of right side tree are indexed ascending from right to left
#                   Will almost 100% have to use recursion
# Video thoughts 1: Uses Depth First Search - recursively iterate finding sum of left and right tree
#                   then return root, left and right
import binarytree
def areSymmetric(root1, root2):
    #condition = True
    # This is the smallest case scenario, when we're at the leaf nodes (no children nodes)
    if root1 is None and root2 is None:
        return True
    # Condition = if root1 or root2 has a child and the other doesn't => False, OR root values != to each other
    elif ((root1 is None) != (root2 is None)) or root1.val != root2.val:
        return False
    else:
    # The smaller problem is making sure left root1 == right root 2, and right root 1 == left root 2
    # Where root 1 is considered to be the left tree/branch, and root 2 is considered to be the right tree/branch
    # return a boolean statement since we are testing if they are equal and both need to be true
    # This way if it returns false at any point, the function carries the False through the recursion
        return areSymmetric(root1.left,root2.right) and areSymmetric(root1.right,root1.left)
def isSymmetric(root):
    # Boundary Case - if none, then its symmetric, if not start actual process
    if root is None:
        return True
    return areSymmetric(root.left, root.right)

if __name__ == '__main__':
    tree = binarytree.tree(0,1,3)
    isSymmetric(tree)

