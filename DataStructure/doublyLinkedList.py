class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None # prev link 추가
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.nodeCount = 0
        
        # 리스트 처음과 끝에 dummy node를 둠
        # 데이터를 담고 있는 node들은 모두 같은 모양이 됨
        self.head = Node(None)
        self.tail = Node(None)
        
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None
    
    
    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr.next.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next.next is not None:
                s += ' -> '
        return s


    def getLength(self):
        return self.nodeCount

        
    def traverse(self): # 리스트 순회
        result = []
        curr = self.head
        while curr.next.next: # dummy tail이 있기 때문에
            curr = curr.next
            result.append(curr.data)
        return result    
    
    
    def reverse(self): # 리스트 역순회
        result = []
        curr = self.tail
        while curr.prev.prev: # dummy head가 있기 때문에
            curr = curr.prev
            result.append(curr.data)
        return result
    

    def getAt(self, pos): # 특정 원소 참조
        if pos < 0 or pos > self.nodeCount:
            return None
        
        if pos > self.nodeCount // 2: # 후반부에 위치할 때
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1
        return curr
        
        
    def insertAfter(self, prev, newNode): # 특정 노드 뒤에 삽입
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True
    
    
    def insertBefore(self, next, newNode): # 특정 노드 앞에 삽입
        prev = next.prev
        return insertAfter(prev, newNode)
    
    
    def insertAt(self, pos, newNode): # 지정된 위치에 새로운 노드 삽입
        if pos < 1 or pos > self.nodeCount + 1:
            return False
            
        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)
        
        
    def popAfter(self, prev): # 특정 노드의 다음 노드 삭제
        curr = prev.next
        prev.next = curr.next
        curr.next.prev = prev
        self.nodeCount -= 1
        return curr.data


    def popBefore(self, next): # 특정 노드의 이전 노드 삭제
        curr = next.prev
        next.prev = curr.prev
        curr.prev.next = next
        self.nodeCount -= 1
        return curr.data
        
        
    def popAt(self, pos): # 지정된 위치의 노드 삭제
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        prev = self.getAt(pos - 1)     
        return self.popAfter(prev)
   
    
    def concat(self, L): # 두 리스트 연결   
        self.tail.prev.next = L.head.next # 원래 리스트의 더미 꼬리를 L의 맨 앞 데이터 노드로 설정
        L.head.next.prev = self.tail.prev # prev 설정
        self.tail = L.tail # 전체 노드의 꼬리를 L의 꼬리로 설정
        self.nodeCount += L.nodeCount 