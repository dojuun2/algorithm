def solution(price, money, count):
    answer = 0
    
    for i in range(1, count + 1):
        answer += price * i

    print(f"answer = {answer}")
    
    if answer > money:
        answer -= money
    else:
        answer = 0
    
    return answer


print(solution(3, 20, 4))