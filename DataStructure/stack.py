class ArrayStack:
    def __init__(self): # 배열을 빈 스택으로 초기화
        self.data = []
    
    def size(self): # 스택 크기 반환
        return len(self.data)
    
    def isEmpty(self): # 스택이 비어 있는지 여부
        return self.size() == 0
        
    def push(self, item): # 데이터 원소 추가
        self.data.append(item)
    
    def pop(self): # 데이터 원소 삭제 후 반환
        return self.data.pop()
        
    def peek(self): # 스택의 top에 있는 원소 반환
        return self.data[-1]