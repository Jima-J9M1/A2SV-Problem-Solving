# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self,root):
        s = []
        def dfs(root):
            if not root:
                  s.append('null')
                  return
            
            s.append(root.val)
            dfs(root.left)
            dfs(root.right)
            
            
        dfs(root)
        
        return ' '.join(str(v) for v in s)

    def deserialize(self, data):
        s = list(data.split())[::-1]
        def dfs(val):
            if val == 'null':
                return
            
            cur = TreeNode(int(val))
            cur.left = dfs(s.pop())
            cur.right = dfs(s.pop())
            return cur
        
        return dfs(s.pop())
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))