# ---------- 내 풀이 ------------
def solution(a, b):
    answer = 0
    
    for a_num, b_num in zip(a, b):
        answer += a_num * b_num
        
    return answer


# ----------- 다른 풀이 -----------
# def solution(a, b):
#     return sum([x * y for x, y in zip(a, b)])


print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
print(solution([-1, 0, 1], [1, 0, -1]))
