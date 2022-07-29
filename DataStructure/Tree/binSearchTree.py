class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        
        
    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self) # node들의 리스트를 생성
        if self.right:
            traversal += self.right.inorder()
        return traversal
        
        
    # left에 가장 작은 값이 있기 때문에 왼쪽으로만 내려가면 최소 값을 찾을 수 있음
    def min(self):
        if self.left: 
            return self.left.min()
        else:
            return self
           
           
    # right에 가장 큰 값이 있기 때문에 오른쪽으로 내려감
    def max(self):
        if self.right: 
            return self.right.max()
        else:
            return self
            
            
    def lookup(self, key, parent = None): # parent node는 없으면 None을 넣어줌
        if key < self.key: # 찾고자 하는 키 값이 더 작다면
            if self.left:
                return self.left.lookup(key, self) # 왼쪽 서브트리에서 다시 찾아봄
            else: # 찾고자 하는 키가 트리에 존재하지 않는 경우
                return None, None 
            elif key > self.key: # 찾고자 하는 키 값이 더 크다면
                if self.right: 
                    return self.right.lookup(key, self) # 오른쪽 서브트리에서 다시 찾아봄
                else:
                    return None, None
            else: # 찾으려는 노드가 발견된 경우
                return self, parent
             
             
    def insert(self, key, data):
        if key < self.key: # 삽입하려는 키 값이 더 작다면 왼쪽 서브트리 확인
            if self.left:
                return self.left.insert(key, data)
            else: # 왼쪽에 노드가 없다면 그 자리에 바로 삽입
                self.left = Node(key, data)
        elif key > self.key: # 삽입하려는 키 값이 더 크다면 오른쪽 서브트리 확인
            if self.right:
                return self.right.insert(key, data)
            else: # 오른쪽에 노드가 없다면 그 자리에 바로 삽입
                self.right = Node(key, data)
        else:
            raise KeyError('Key %s already exists.' % key) # 중복된 값은 삽입할 수 없음 - 예외 발생
            
            
    def countChildren(self): # child node 개수 카운트
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count
            
            
    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countChildren()
            # The simplest case of no children
            if nChildren == 0:
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # parent.left 또는 parent.right 를 None 으로 하여
                # leaf node 였던 자식을 트리에서 끊어내어 없앱니다.
                if parent:
                    if node is parent.left:
                        parent.left = None
                    else:
                        parent.right = None
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 를 None 으로 하여 빈 트리로 만듭니다.
                else:
                    self.root = None
            # When the node has only one child
            elif nChildren == 1:
                # 하나 있는 자식이 왼쪽인지 오른쪽인지를 판단하여
                # 그 자식을 어떤 변수가 가리키도록 합니다.
                if node.left != None:
                    child = node.left
                else:
                    child = node.right
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # 위에서 가리킨 자식을 대신 node 의 자리에 넣습니다.
                if parent:
                    if node == parent.left:
                        parent.left = child
                    else:
                        parent.right = child
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 에 위에서 가리킨 자식을 대신 넣습니다.
                else:
                    self.root = child
            # When the node has both left and right children
            else:
                parent = node
                successor = node.right
                # parent 는 node 를 가리키고 있고,
                # successor 는 node 의 오른쪽 자식을 가리키고 있으므로
                # successor 로부터 왼쪽 자식의 링크를 반복하여 따라감으로써
                # 순환문이 종료할 때 successor 는 바로 다음 키를 가진 노드를,
                # 그리고 parent 는 그 노드의 부모 노드를 가리키도록 찾아냅니다.
                while successor.left:
                    parent = successor
                    successor = successor.left
                # 삭제하려는 노드인 node 에 successor 의 key 와 data 를 대입합니다.
                node.key = successor.key
                node.data = successor.data
                # 이제, successor 가 parent 의 왼쪽 자식인지 오른쪽 자식인지를 판단하여
                # 그에 따라 parent.left 또는 parent.right 를
                # successor 가 가지고 있던 (없을 수도 있지만) 자식을 가리키도록 합니다.
                if successor == parent.left:
                    parent.left = successor.right
                else:
                    parent.right = successor.right
            return True
        else:
            return False
                
        
        
class BinSearchTree:

    def __init__(self): 
        self.root = None # 빈 트리로 초기화
        
        
    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []
            
            
    def min(self):
        if self.root:
            return self.root.min()
        else:
            return None
        
    
    def max(self):
        if self.root:
            return self.root.max()
        else:
            return None
        
        
    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None
            
            
    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)
            
            
    def remove(self, key): # key를 입력으로 받음
        node, parent = self.lookup(key)
        if node:
            return True # 삭제한 경우
        else:
            return False # 해당 키의 노드가 없는 경우