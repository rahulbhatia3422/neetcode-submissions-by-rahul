# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []      # nodes store karne ke liye
        curr = root     # current node
        
        while stack or curr:
            # LEFT MOST node tak jaao
            while curr:
                stack.append(curr)  # baad me process karne ke liye
                curr = curr.left    # left ki taraf badho
            
            # Ab stack ke top pe smallest available node hai
            curr = stack.pop()  # nikal lo smallest node
            
            # Check karo kya ye kth smallest hai?
            k -= 1      # ek node process ho gaya
            if k == 0:  # agar kth node mil gaya
                return curr.val  # answer return kardo
            
            # Right subtree me jao
            curr = curr.right


            