# ---------- 내가 푼 방법 -------------
def solution(n):
    answer = 0

    while n >= 1:
        answer += n % 10
        n //= 10

    return answer


# ----------- 다른 방법 -------------
# def solution(n):
#     answer = sum([int(i) for i in str(n)])

#     return answer

# def solution(n):
#     answer = 0
#     if n < 10:
#         return n

#     answer = n % 10 + solution(n // 10)
    
#     return answer


solution(9)
