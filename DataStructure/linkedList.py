class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None
        
    def __repr__(self): # 연결리스트 객체 표현
        if self.nodeCount == 0:
            return 'LinkedList is empty'
        s = ''
        cur = self.head
        while cur is not None:
            s += repr(cur.data) # 객체를 문자열로 변환
            if cur.next is not None:
                s += ' -> '
            cur = cur.next
        return s

    def getAt(self, pos): # 특정 원소 참조
        if pos <= 0 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self): # 리스트 순회
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result
    
    def insertAt(self, pos, newNode): # 새로운 노드 삽입
        if pos < 1 or pos > self.nodeCount + 1:
            return False
            
        if pos == 1: # 리스트 맨 앞에 삽입할 때 : O(1)
            newNode.next = self.head # 헤드 앞에 삽입
            self.head = newNode # 새로운 헤드로 지정
            
        else:
            if pos == self.nodeCount + 1:
                prev = self.tail # 이전 노드를 따로 찾을 필요 없음
            else:
                prev = self.getAt(pos - 1) # 이전 노드
            newNode.next = prev.next # prev와 prev.next 사이에 삽입 : O(n)
            prev.next = newNode
            
        if pos == self.nodeCount + 1: # 리스트 맨 뒤에 삽입할 때 : O(1)
            self.tail = newNode # 새로운 테일로 지정
        
        self.nodeCount += 1
        return True
        
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
            
        cur = self.getAt(pos)
        if pos == 1: # 맨 앞에서 삭제 : O(1)
            if self.nodeCount == 1: # 유일한 값을 삭제할 경우
                self.head = None
                self.tail = None
            else:
                self.head = cur.next
        else: # 중간, 맨 끝에서 삭제 : O(n)
            prev = self.getAt(pos - 1)
            prev.next = cur.next
            if pos == self.nodeCount:
                self.tail = prev
                
        self.nodeCount -= 1
        return cur.data
    
    def concat(self, L): # 두 리스트 연결   
        self.tail.next = L.head # 기존 리스트의 꼬리와 L의 머리를 연결
        if L.tail is not None: # L의 꼬리가 None이 아닌 경우
            self.tail = L.tail # L의 꼬리가 전체 꼬리가 됨
        self.nodeCount += L.nodeCount # L의 노드 수를 추가해서 더함