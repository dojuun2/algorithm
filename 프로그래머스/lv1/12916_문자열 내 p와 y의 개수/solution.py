# --------- 내 풀이 ------------
def solution(s):
    answer = True
    p_count, y_count = 0, 0

    for i in s:
        if i == "y" or i == "Y":
            y_count += 1
        elif i == "P" or i == "p":
            p_count += 1
            
    if y_count != p_count:
        answer = False
        
    print(answer)

    return answer


# -------------- 다른 풀이 ---------------
# def solution(s):
#     answer = True
    
#     # lower()
#     # 문자열 모든 문자 소문자로
    
#     # count()
#     # 문자열 안의 특정 문자 개수
    
#     s = s.lower()   # 모든 문자 소문자로
#     p = s.count('p')
#     y = s.count('y')
    
#     if p != y:
#         answer = False
        
#     print(answer)
    
#     return answer


# def solution(s):
#     answer = True
    
#     answer = s.lower().count('p') == s.lower().count('y')
#     print(answer)
    
#     return answer
    

solution("pPoooyY")
solution("Pyy")