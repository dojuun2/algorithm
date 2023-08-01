def solution(d, budget):
    answer = 0
    d.sort()
    
    for i in d:
        if budget - i < 0: break
        budget = budget - i
        answer += 1
        
    return answer


print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))
