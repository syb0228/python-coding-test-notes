from doublyLinkedList import Node, DoublyLinkedList

class PriorityQueue:

    def __init__(self):
        self.queue = DoublyLinkedList()

    def size(self):
        return self.queue.getLength()

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, x):
        newNode = Node(x)
        curr = self.queue.head # 처음 위치 지정
        # while 종료 조건 : 연결 리스트의 끝이거나, 다음 노드의 데이터보다 값이 크거나 같은 경우
        while curr.next.data != None and x < curr.next.data:
            curr = curr.next
        self.queue.insertAfter(curr, newNode) # 해당 위치 다음에 삽입

    def dequeue(self):
        return self.queue.popAt(self.queue.getLength())

    def peek(self):
        return self.queue.getAt(self.queue.getLength()).data
        