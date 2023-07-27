# ---------- 내 풀이 -----------
# def solution(left, right):
#     answer = 0
    
#     for num in range(left, right + 1):
#         count = 0
        
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 count += 1
                
#         if count % 2:
#             answer -= num
#         else:
#             answer += num
        
#     return answer


# ---------- 다른 풀이 -----------
def solution(left, right):
    # 약수의 개수가 홀수인 수는 제곱수
    answer = 0
    
    for i in range(left, right + 1):
        if int(i**0.5) == i**0.5:
            answer -= i
        else:
            answer += i
    
    return answer


# import math
# def solution(left, right):
#     # 약수의 개수가 홀수인 수는 제곱수
#     answer = 0
    
#     for i in range(left, right + 1):
#         sqrt = math.sqrt(i)     # i의 제곱근
#         if int(sqrt) == sqrt:
#             answer -= i
#         else:
#             answer += i
    
#     return answer


print(solution(13, 17))
print(solution(24, 27))