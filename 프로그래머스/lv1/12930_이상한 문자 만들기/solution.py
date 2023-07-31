# ----------- 내 풀이 -------------
# def solution(s):
#     answer = ''

#     s_list = s.split(' ')
    
#     for i in s_list:
#         for j in range(len(i)):
#             if j % 2:
#                 answer += i[j].lower()
#             else:
#                 answer += i[j].upper()
#         answer += ' '
        
#     return answer[0:len(answer) - 1]


# ------------ 다른 풀이 -------------
def solution(s):
    answer = []
    
    for i in s.split(' '):
        word = ''

        for j in range(len(i)):
            word += i[j].upper() if j % 2 == 0 else  i[j].lower()
            # if j % 2 == 0:
            #     word += i[j].upper()
            # else:
            #     word += i[j].lower()
                
        answer.append(word)
    
    print(answer)
    return ' '.join(answer)
    
    
print(solution("try hello world"))
print(solution("world"))