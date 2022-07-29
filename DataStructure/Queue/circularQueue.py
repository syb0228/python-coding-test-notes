class CircularQueue:

    def __init__(self, n): # 빈 큐 초기화
        self.maxCount = n # 인자로 주어진 최대 큐 길이 설정
        self.data = [None] * n
        self.count = 0 # 현재 큐에 들어있는 데이터 원소 개수
        self.front = -1
        self.rear = -1
        
    def size(self): # 현재 큐 길이 반환
        return self.count
        
    def isEmpty(self):
        return self.count == 0
       
    def isFull(self):
        return self.count == self.maxCount # 최대 큐 길이와 비교
        
    def enqueue(self, x): # 큐에 데이터 원소 추가
        if self.isFull(): # 큐가 꽉차있는 경우 예외 발생
            raise IndexError('Queue full')
        self.rear = (self.rear + 1) % self.maxCount # pointer 조정
        self.data[self.rear] = x # 데이터 추가
        self.count += 1 # 카운트 증가
        
    def dequeue(self): # 큐에서 데이터 원소 뽑기
        if self.isEmpty(): # 큐가 비어있는 경우 예외 발생
            raise IndexError('Queue empty')
        self.front = (self.front + 1) % self.maxCount
        x = self.data[self.front]
        self.count -= 1
        return x
        
    def peek(self): # 큐의 맨 앞 원소 들여다보기
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[(self.front + 1) % self.maxCount]