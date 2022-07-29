class Maxheap:

    def __init__(self): # empty heap 생성
        self.data = [None]
        
        
    def insert(self, item):
        child = len(self.data) # 새로운 원소의 위치
        parent = child // 2 # 새로운 원소의 부모 노드의 위치
        self.data.append(item) # 마지막 자리에 새로운 원소 임시 저장
        
        while child > 1:
            if self.data[child] > self.data[parent]: # 부모 노드와 키 값을 비교
                # 더 크면 부모 노드와 위치를 변경
                self.data[child], self.data[parent] = self.data[parent], self.data[child]
            else:
                break
            child = parent
            parent = child // 2
    
    
    def remove(self):
        if len(self.data) > 1:
            # 트리 마지막 자리 노드를 임시로 루트 노드 자리에 배치
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1) # 최댓값 삭제
            self.maxHeapify(1) # 재귀 호출로 max heap 조건 만족
        else:
            data = None
        return data
        
            
    def maxHeapify(self, i):
        left = i * 2 # left child 인덱스 계산
        right = i * 2 + 1 # right child 인덱스 계산
        smallest = i # 자기 자신으로 초기화
        
        # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 키 값이 자신보다 더 큰지를 판단
        if left < len(self.data) and self.data[left] > self.data[smallest]:
            smallest = left # smallest는 왼쪽 자식의 인덱스를 갖게 됨

        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 키 값이 오른쪽 자식 또는 자기 자신보다 더 큰지를 판단
        if right < len(self.data) and self.data[right] > self.data[smallest]:
            smallest = right # smallest는 오른쪽 자식의 인덱스를 갖게 됨

        if smallest != i: # 나보다 큰 값을 가진 자식 노드를 발견한 경우
            # 현재 노드(인덱스 i)와 최댓값 노드(왼쪽 아니면 오른쪽 자식)를 교체
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]

            # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리함
            self.maxHeapify(smallest)
        
        
    def heapsort(unsorted):
        H = MaxHeap()
        for item in unsorted: # 정렬되지 않은 원소들을 전부 최대 힙에 삽입
            H.insert(item)
        
        sorted = []
        d = H.remove()
        while d: # 힙이 빌 때까지
            sorted.append(d) # 원소들을 하나씩 삭제하고 삭제된 원소들을 새로운 리스트에 저장
            d = H.remove()
        return sorted