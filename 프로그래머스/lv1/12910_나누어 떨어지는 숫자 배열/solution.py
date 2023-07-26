# ---------- 내 풀이 ------------
def solution(arr, divisor):
    answer = []

    for n in arr:
        if n % divisor == 0:
            answer.append(n)

    if len(answer) == 0:
        answer.append(-1)

    answer.sort()

    return answer


# ---------- 다른 풀이 ------------
# def solution(arr, divisor):
#     answer = sorted([n for n in arr if n % divisor == 0]) or [-1]

#     return answer


# def solution(arr, divisor):
#     answer = [n for n in arr if n % divisor == 0]
#     answer.sort()

#     return answer or [-1]


# def solution(arr, divisor):
#     answer = [n for n in arr if n % divisor == 0]
#     answer.sort()

#     if answer == []:
#         answer.append(-1)
        
#     return answer


print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3, 2, 6], 10))
