class BinaryTreeNode(object):
    def __init__(self, data):
        self.Data = data
        self.Left = None
        self.Right = None

class BinarySearchTree(object):

    def __init__(self):
        self._root = None
    
    def preorder(self):
        if not self._root:
            return []
        
        return self._preorder(self._root, [])
    
    def _preorder(self, node:BinaryTreeNode, acc=[]):
        acc.append(node.Data)

        if node.Left:
            acc = self._preorder(node.Left, acc)
        
        if node.Right:
            acc = self._preorder(node.Right, acc)
        
        return acc

    def inorder(self):
        if not self._root:
            return []

        return self._inorder(self._root, [])

    def _inorder(self, node:BinaryTreeNode, acc=[]):
        if node.Left:
            acc = self._inorder(node.Left, acc)

        acc.append(node.Data)

        if node.Right:
            acc = self._inorder(node.Right, acc)
        
        return acc
    
    def postorder(self):
        if not self._root:
            return []
        
        return self._postorder(self._root, [])

    def _postorder(self, node:BinaryTreeNode, acc=[]):
        if node.Left:
            acc = self._postorder(node.Left, acc)

        if node.Right:
            acc = self._postorder(node.Right, acc)
        
        acc.append(node.Data)

        return acc

    def size(self):
        if not self._root:
            return 0
        
        return self._size(self._root)
    
    def _size(self, node, count=0):
        left  = self._size(node.Left, count + 1) if node.Left else 0
        right = self._size(node.Right, count + 1) if node.Right else 0

        return left + right + 1
    
    def insert(self, data):
        if not self._root:
            self._root = BinaryTreeNode(data)
        else:
            self._insert(self._root, data)
    
    def _insert(self, node : BinaryTreeNode, data):
        if data < node.Data:
            if node.Left:
                self._insert(node.Left, data)
            else:
                node.Left = BinaryTreeNode(data)

        if data > node.Data:
            if node.Right:
                self._insert(node.Right, data)
            else:
                node.Right = BinaryTreeNode(data)