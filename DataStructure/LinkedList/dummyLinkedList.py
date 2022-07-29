class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None) # 맨 앞에 dummy node 추가
        self.tail = None
        self.head.next = self.tail
        
        
    def traverse(self): # 리스트 순회
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result    


    def getAt(self, pos): # 특정 원소 참조
        if pos < 0 or pos > self.nodeCount:
            return None
        i = 0 # getAt(0) -> head
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr
        
        
     def insertAfter(self, prev, newNode): # 특정 노드 뒤에 삽입
        newNode.next = prev.next
        if prev.next is None: # 맨 마지막에 삽입하는 경우
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True
    
    
    def insertAt(self, pos, newNode): # 새로운 노드 삽입 - insertAfter 함수 활용
        if pos < 1 or pos > self.nodeCount + 1:
            return False
            
        # empty node가 아니고 tail 뒤에 삽입하는 경우    
        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)
        
        
    def popAfter(self, prev): # 특정 노드 뒤의 노드 삭제
        curr = prev.next
        if curr == None: # prev가 마지막 노드일 때
            return None
        if curr.next == None: # 리스트 맨 끝의 node를 삭제할 때
            self.tail = prev
        prev.next = curr.next
        self.nodeCount -= 1
        return curr.data
        
        
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        prev = self.getAt(pos - 1)     
        return self.popAfter(prev)
   
    
    def concat(self, L): # 두 리스트 연결   
        self.tail.next = L.head.next # 기존 리스트의 꼬리와 L의 머리 다음 노드를 연결
        if L.tail: # L의 꼬리가 None이 아닌 경우
            self.tail = L.tail # L의 꼬리가 전체 꼬리가 됨
        self.nodeCount += L.nodeCount # L의 노드 수를 추가해서 더함