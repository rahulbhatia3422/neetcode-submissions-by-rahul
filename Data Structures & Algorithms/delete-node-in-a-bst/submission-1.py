# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # Base case: if the tree is empty, nothing to delete
        if not root:
            return None
        
        # ---- Search phase: locate the node to delete ----
        if key < root.val:
            # Key is in the left subtree; recursively delete and update left child
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # Key is in the right subtree; recursively delete and update right child
            root.right = self.deleteNode(root.right, key)
        else:
            # ---- Node found (root.val == key) ----
            # Case 1: node has no left child (covers leaf and only right child)
            if not root.left:
                # Replace this node with its right child (could be None)
                return root.right
            # Case 2: node has no right child (only left child)
            if not root.right:
                # Replace this node with its left child
                return root.left
            
            # Case 3: node has two children
            # ---- Find the inorder successor (smallest in the right subtree) ----
            successor = root.right               # start at right child
            while successor.left:                # keep going left until no left child
                successor = successor.left       # successor will have no left child
            
            # Copy the successor's value into the current node
            root.val = successor.val
            
            # ---- Delete the inorder successor from the right subtree ----
            # The successor is guaranteed to have no left child,
            # so this recursive call will hit case 1 or 2 (easy deletion).
            root.right = self.deleteNode(root.right, successor.val)
        
        # Return the (possibly modified) root of this subtree
        return root

# Alternative Approach 

            # Find inorder predecessor (largest in left subtree)
            # predecessor = root.left
            # while predecessor.right:
            #     predecessor = predecessor.right
            
            # root.val = predecessor.val
            # root.left = self.deleteNode(root.left, predecessor.val)
        