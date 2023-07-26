# ---------- 내 풀이 -------------
def solution(numbers):
    answer = 0
    
    for i in range(1, 10):
        if i not in numbers:
            answer += i

    return answer


# ------------ 다른 풀이 --------------
# def solution(numbers):
#     answer = sum(range(1, 10)) - sum(numbers)
    
#     return answer


# def solution(numbers):
#     answer = sum([i for i in range(0, 10) if i not in numbers])
    
#     return answer


print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))