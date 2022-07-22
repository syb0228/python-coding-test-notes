def binary_search(L, x):
    lower = 0
    upper = len(L) - 1
    answer = -1
    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x:
            answer = middle
            break # 수행 시간 효율성을 위해 추가
        elif L[middle] < x:
            lower = middle + 1
        else:
            upper = middle - 1
    return answer

L = [3, 8, 2, 7, 6, 10, 9]
L.sort() # 이진탐색은 리스트가 정렬된 경우에만 가능
print(L)
print(binary_search(L, 6))
print(L.index(6))