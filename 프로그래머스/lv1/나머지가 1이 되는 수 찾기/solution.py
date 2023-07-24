# ----------- 내 풀이 ------------
def solution(n):
    for x in range(2, n + 1):
        if n % x == 1:
            print(x)
            return x
        
# ---------- 다른 풀이 ------------
# def solution(n):
#     answer = min([x for x in range(2, n+1) if n % x == 1])
#     print(answer)
#     return answer
    
    
solution(10)
solution(12)