# ---------- 내 풀이 -------------
def solution(n):
    answer = 0
    
    x = n**0.5
    if x == int(x):
        answer = (x+1)**2
    else:
        answer = -1

    print(answer)
    return answer

# ----------- 다른 풀이 ------------- 
# def solution(n):
    # answer = 0
    
    # x = n**0.5
    # if n == x**2:
    #     answer = (x+1)**2
    # else:
    #     answer = -1

    # print(answer)
    # return answer


solution(121)
solution(3)