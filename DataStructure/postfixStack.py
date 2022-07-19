class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    answer = ''
    opStack = ArrayStack()
    for s in S: # 중위 표현식을 왼쪽부터 한 글자씩 읽음   
        if s == '(': # 여는 괄호이면 stack에 push
            opStack.push(s)
        elif s == ')': # 닫는 괄호이면
            while True: # 여는 괄호가 나올 때까지 스택에서 pop, 출력
                v = opStack.pop() 
                if v == '(': 
                    break
                answer += v
        elif s not in prec: # 피연산자이면 그냥 출력
            answer += s
        else: # 연산자이면
            if opStack.isEmpty(): # 스택이 비어 있다면 해당 연산자를 스택에 바로 push
                opStack.push(s)
            else: # 스택이 비어 있지 않다면 연산자 우선 순위 비교
                while not opStack.isEmpty():
                    v = opStack.peek() # 스택 맨 위에 있는 값을 가져옴
                    if prec[v] >= prec[s]: # 해당 연산자보다 높거나 같은 우선순위를 가진 것들이라면 pop, 출력
                        v2 = opStack.pop()
                        answer += v2   
                    else:
                        break # 우선순위가 더 낮다면 반복 비교문 종료
                opStack.push(s) # 해당 연산자를 스택에 push
                        
    while not opStack.isEmpty(): # stack에 남아 있는 연산자를 모두 pop, 출력
        v = opStack.pop()
        answer += v                                   
    
    return answer