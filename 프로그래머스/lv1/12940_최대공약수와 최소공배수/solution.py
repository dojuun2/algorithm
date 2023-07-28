def solution(n, m):
    answer = []

    x, y = n, m
    while(True):
        x, y= y, x % y
        if y == 0: 
            answer.append(x)
            break

    answer.append((n * m) // answer[0])

    return answer


# def solution(n, m):
#     # 유클리드 호제법
#     # x, y의 최대공약수는 y, r(x를 y로 나눈 나머지 값)의 최대공약수와 같다.
#     x, y = n, m
#     while y > 0:
#         x, y = y, x % y

#     answer = [x, (n * m) // x]

#     return answer


print(solution(3, 12))
print(solution(2, 5))