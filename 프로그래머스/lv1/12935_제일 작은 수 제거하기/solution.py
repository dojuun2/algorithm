# ----------- 내 풀이 ------------
def solution(arr):
    answer = arr
    
    answer.remove(min(arr))
    
    if answer == []:
        answer.append(-1)
    
    return answer


# ------------- 다른 풀이 ------------
# def solution(arr):
#     arr.remove(min(arr))    
#     return arr or [-1]


print(solution([4,3,2,1]))
print(solution([10]))