from doublyLinkedList import Node
from doublyLinkedList import DoublyLinkedList

class LinkedListStack:
    def __init__(self): # 양방향리스트를 스택으로 초기화
        self.data = DoublyLinkedList()
    
    def size(self):
        return self.data.getLength()
    
    def isEmpty(self):
        return self.size() == 0
    
    def push(self, item):
        node = Node(item) # 새로운 노드 생성
        self.data.insertAt(self.size() + 1, node) # 맨 뒤에 삽입
    
    def pop(self):
        return self.data.popAt(self.size()) # 맨 뒤 노드 삭제 후 리턴
    
    def peek(self):
        return self.data.getAt(self.size()).data # 맨 뒤 노드 리턴