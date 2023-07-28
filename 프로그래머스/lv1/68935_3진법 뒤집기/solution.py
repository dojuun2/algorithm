def solution(n):
    answer = ''
    
    # 10진법 숫자를 3으로 나누어 그 나머지를 표시하고 더이상 나눌 수 없을 때까지 반복하면 됨    
    while(n > 0):
        answer += str(n % 3)
        n //= 3
    
    return int(answer, 3)


print(solution(45))
print(solution(125))