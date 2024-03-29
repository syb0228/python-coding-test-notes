import heapq

# 내림차순 힙 정렬 (heap sort)
def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, -value) # 데이터의 부호를 바꿔서 넣음
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(-heapq.heappop(h)) # 데이터의 부호를 바꿔서 꺼냄
  return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)