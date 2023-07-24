# ------------ 내 풀이 -------------
def solution(arr):
    answer = 0
    
    for i in arr:
        answer += i
    
    answer /= len(arr)
    print(answer)
    
    return answer

# ---------------- 다른 풀이 ----------------
# def solution(arr):
#     answer = sum(arr) / len(arr)
#     print(answer)
    
#     return answer


solution([1,2,3,4])