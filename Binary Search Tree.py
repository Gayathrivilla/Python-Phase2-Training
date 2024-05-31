class solution(object):
    def insertintoBST(self,root,val):
        if root==None:
            return Treenode(val)
        elif root.val>val:
            root.left=self.insertintoBST(root.left,val)
        else:
            root.right=self.insertintoBST(root.right,val)
        return root