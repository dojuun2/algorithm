# -------- 내 풀이 ----------
# def solution(seoul):
#     answer = ''
    
#     for i in range(len(seoul)):
#         if seoul[i] == "Kim":
#             answer = f'김서방은 {i}에 있다'
#             break
    
#     return answer


# --------- 다른 풀이 -----------
def solution(seoul):
    answer = f'김서방은 {seoul.index("Kim")}에 있다'

    return answer


print(solution(["Jane", "Kim"]))