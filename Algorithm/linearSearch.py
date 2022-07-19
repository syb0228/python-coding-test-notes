def linear_search(S, x):
    i = 0
    while i < len(S) and S[i] != x:
        i += 1
    if i < len(S):
        return i
    else:
        return -1

S = [3, 8, 2, 7, 6, 10, 9]
print(linear_search(S, 7)) # 3
print(S.index(7)) # 3