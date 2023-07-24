def solution(n):
    answer = list(str(n))
    answer.sort(reverse=True)
    print(int("".join(answer)))
    
    return int("".join(answer))


solution(118372)