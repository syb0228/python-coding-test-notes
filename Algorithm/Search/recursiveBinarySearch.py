def binary_search(L, x, lower, upper):
    if lower > upper:
        return -1
    mid = (lower + upper) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return binary_search(L, x, lower, mid -1)
    else:
        return binary_search(L, x, mid + 1, upper)
        
L = [1, 3, 5, 6, 9, 13, 17, 25]
print(binary_search(L, 17, 0, len(L) - 1)) # 6