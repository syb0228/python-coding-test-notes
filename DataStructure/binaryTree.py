class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]

class Node:
    def __init__(self, item):
        self.data = item
        self.left = None # left child
        self.right = None # right child
        
    # 재귀적으로 구할 수 있음
    # 전체 이진 트리 size() = left subtree size() + right subtree size() + 1(자기자신)
    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1
        
    # 전체 이진 트리의 depth() = left subtree depth()와 right subtree depth() 중 더 큰 것 + 1
    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        if l > r:
            d = l
        else:
            d = r
        return d + 1
        
    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal
        
    def preorder(self):
        traversal = []
        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal
        
    def postorder(self):
        traversal = []
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal
        
        
class BinaryTree:
    def __init__(self, r):
        self.root = r # root만 알고 있으면 됨
        
    def size(self):
        if self.root:
            return self.root.size()
        else: # empty tree인 경우
            return 0
              
    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0
            
    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []
            
    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []
    
    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []
            
            
    def bft(self): # 넓이 우선 순회
        traversal = []
        q = ArrayQueue()
        
        if self.root: # 빈 트리가 아니면 root node를 q에 추가
           q.enqueue(self.root)
           
        while not q.isEmpty(): # q가 비어 있지 않는 동안
            # q에서 추출한 node 방문
            node = q.dequeue()
            traversal.append(node.data)
            # node의 left, right child가 있으면 q에 추가
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)  
                
        return traversal
        
        