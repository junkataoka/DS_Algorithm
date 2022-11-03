def __main__():

   # Definition for a binary tree node.
   class TreeNode:
      def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


   def helper(root, res):
      if root != None:
          helper(root.left, res)
          res.append(root.val)
          helper(root.right, res)


   def inorderTraversal(root):
      res = []
      helper(root, res)

      return res

   def inorderTraversalIterative(root):
      stack = []
      res = []
      curr = root
      # Condition1-1: current node is empty
      # Condition1-2: stack is empty
      # Then we are done
      while curr or stack:
         # If the current node exists, push it into the stack
         # then mode to its left child
         if curr:
            stack.append(curr)
            curr = curr.left

         else:
            # Otherwise, if the current node is None, pop and element from
            # the stack, and finally set teh current node to its right child
            # Move of left node
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

      return res

  # Test case
   tree = TreeNode(val=10, left=None, right=None)
   tree.left = TreeNode(val=30)
   tree.right = TreeNode(val=20)
   tree.right.left = TreeNode(val=1)
   tree.right.right = TreeNode(val=5)
   print(inorderTraversal(tree))
   print(inorderTraversalIterative(tree))

if __name__ == "__main__":
   __main__()
