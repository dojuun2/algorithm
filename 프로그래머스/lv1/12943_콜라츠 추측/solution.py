# -------- 내 풀이 ----------
def solution(num):
    answer = 0

    if num != 1:
        while num > 1:
            if num % 2 == 0:
                num /= 2
            else:
                num = num * 3 + 1
            answer += 1

            if answer >= 500:
                answer = -1
                break

    return answer


print(solution(6))
print(solution(16))
print(solution(626331))
