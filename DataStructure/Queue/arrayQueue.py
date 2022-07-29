class ArrayQueue:
    def __init__(self):
        self.data = []
    
    def size(self): # O(1)
        return len(self.data)
       
    def isEmpty(self): # O(1)
        return self.size() == 0
        
    def enqueue(self, item): # O(1)
        self.data.append(item)
        
    def dequeue(self): # O(n) : worst case - 배열의 맨 앞 원소를 꺼내는 경우
        return self.data.pop(0)
        
    def peek(self): # O(1)
        return self.data[0]