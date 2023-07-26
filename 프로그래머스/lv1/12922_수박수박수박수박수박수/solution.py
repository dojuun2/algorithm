# ---------- 내 풀이 -----------
# def solution(n):
#     answer = ''

#     for i in range(1, n + 1):
#         if i % 2:
#             answer += '수'
#         else:
#             answer += '박'

#     return answer


# ----------- 다른 풀이 ----------
def solution(n):
    # n = 3
    # 수박수박수박
    # => 수박수박수박 + 수
    
    # n = 4
    # 수박수박수박수박
    # => 수박수박수박수박 + 0
    return "수박" * (n // 2) + "수" * (n % 2)


print(solution(3))
print(solution(4))
