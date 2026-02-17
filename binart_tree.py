from collections import deque
'''
      4
    /   \
   2     6
  / \   / \
 1   3 5   7
 [1, 2, 3, 4, 5, 6, 7]
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        left_val = self.left.val if self.left else "None"     # inline comment
        right_val = self.right.val if self.right else "None"  # inline comment
        return f"{self.val}\n/   \\\n{left_val}   {right_val}" # inline comment

    __repr__ = __str__  # inline comment: so typing root in console also shows same
    
def build_tree(level):
    if not level or level[0] is None:
        return None
    root = TreeNode(level[0])
    q = deque([root])
    i = 1
    while q and i < len(level):
        node = q.popleft()
        if i < len(level) and level[i] is not None:
            node.left = TreeNode(level[i])
            q.append(node.left)
        i += 1
        if i < len(level) and level[i] is not None:
            node.right = TreeNode(level[i])
            q.append(node.right)
        i += 1
    return root

# Example input:
root = build_tree([5, 3, 7, 1, 4, None, 8, None, None, 6])
# print(Solution().inorderTraversal(root))  # [1, 3, 2]

class Solution:
    def inorderTraversal(self, root):
        res = []                                   # output
        stack = []                                 # manual call stack
        cur = root                                 # pointer

        while cur or stack:                        # still have nodes to process
            while cur:                             # go as left as possible
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()                      # visit the leftmost not visited node
            res.append(cur.val)                    # record inorder visit
            cur = cur.right                        # then go right
        return res
print(Solution().inorderTraversal(root))  # [1, 2, 3, 4, 5, 6, 7]