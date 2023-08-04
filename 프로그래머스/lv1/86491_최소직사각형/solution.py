# 완전탐색

# ----------- 내 풀이 -----------
def solution(sizes):
    size_list = list()
    for size in sizes:
        size.sort()
        if len(size_list) == 0:
            size_list.append(size[0])
            size_list.append(size[1])
            continue
        
        if size_list[0] < size[0]: size_list[0] = size[0]
        if size_list[1] < size[1]: size_list[1] = size[1]
        
    print(size_list)
            
    return size_list[0] * size_list[1]


# ----------- 다른 풀이 ------------
# def solution(sizes):
#     return max(max(i) for i in sizes) * max(min(i) for i in sizes)


# def solution(sizes):
#     min_size, max_size = 0, 0
#     for i, j in sizes:
#         if i > j:
#             i, j = j, i
        
#         min_size = max(min_size, i)
#         max_size = max(max_size, j)
                
#     return min_size * max_size
    

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
