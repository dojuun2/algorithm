# ------------ 내 풀이 ------------
def solution(a, b):
    answer = 0

    if b >= a:
        for n in range(a, b+1):
            answer += n
    elif a > b:
        for n in range(b, a+1):
            answer += n

    return answer


# ------------ 다른 풀이 ------------
# def solution(a, b):
#     answer = 0

#     if a > b:
#         a, b = b, a

#     answer = sum(range(a, b + 1))
#     return answer


# def solution(a, b):
#     answer = 0

#     answer = sum(range(min(a, b), max(a, b) + 1))
#     return answer


print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))
