# --------- 내 풀이 ------------
def solution(s):
    
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()
    
    return False
        

# --------- 다른 풀이 ------------
# def solution(s):
#     return s.isdigit() and len(s) in [4, 6]


# def solution(s):
#     return s.isdigit() and (len(s) == 4 or len(s) == 6)


# def solution(s):
#     answer = True
    
#     if len(s) == 4 or len(s) == 6:
#         try:
#             int(s)
#         except:
#             answer = False
#     else:
#         answer = False
    
#     return answer


print(solution("a234"))
print(solution("1234"))