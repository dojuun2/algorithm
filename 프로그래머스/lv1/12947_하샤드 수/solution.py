# ----------- 내 풀이 ------------
def solution(x):
    answer = True

    x_list = [int(i) for i in str(x)]
    if x % sum(x_list):
        answer = False
    
    return answer


# -------- 다른 풀이 -----------
def solution(x):
    return x % sum(int(i) for i in str(x)) == 0


solution(10)
solution(12)
solution(11)
solution(13)