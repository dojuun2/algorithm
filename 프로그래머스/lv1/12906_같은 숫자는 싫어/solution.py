# --------- 내 풀이 ---------
def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        else:
            if arr[i] != arr[i - 1]:
                answer.append(arr[i])
    
    return answer


# ---------- 다른 풀이 -----------
# def solution(arr):
#     answer = arr[0]
    
#     for i in arr:
#         if answer[-1] == i: continue
#         answer.append(i)

#     return answer


# def solution(arr):
#     answer = []
    
#     for i in arr:
#         if len(answer) == 0 or answer[-1] != i:
#             answer.append(i)

#     return answer


print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))