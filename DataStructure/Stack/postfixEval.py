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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    
    for token in tokenList:
        if type(token) is int:
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            while True:
                v = opStack.pop()
                if v == '(':
                    break
                postfixList.append(v)
        else:
            if opStack.isEmpty():
                opStack.push(token)
            else:
                while not opStack.isEmpty():
                    v = opStack.peek()
                    if prec[v] >= prec[token]:
                        v1 = opStack.pop()
                        postfixList.append(v1)
                    else:
                        break
                opStack.push(token)
                
    while not opStack.isEmpty():
        v = opStack.pop()
        postfixList.append(v)
        
    return postfixList


def postfixEval(tokenList): # 후위 표기 수식 계산
    valStack = ArrayStack()
    
    for token in tokenList: # 후위 표현식을 왼쪽부터 한 글자씩 읽음
        if type(token) is int: # 피연산자이면 stack에 push
            valStack.push(token) 
        elif token == '*': # 연산자이면
            v1 = valStack.pop() # pop (1)
            v2 = valStack.pop() # pop (2)
            valStack.push(v2 * v1) # (2) 연산 (1) 계산 결과를 push
        elif token == '/':
            v1 = valStack.pop()
            v2 = valStack.pop()
            valStack.push(v2 / v1)
        elif token == '+':
            v1 = valStack.pop()
            v2 = valStack.pop()
            valStack.push(v2 + v1)
        elif token == '-':
            v1 = valStack.pop()
            v2 = valStack.pop()
            valStack.push(v2 - v1)
            
    return valStack.pop() # 수식의 끝에 도달하면 stack에서 pop => 최종 연산 결과


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val