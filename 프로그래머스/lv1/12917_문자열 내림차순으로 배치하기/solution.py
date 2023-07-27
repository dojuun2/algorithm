# --------- 내 풀이 ----------
def solution(s):
    answer = "".join(sorted(s, reverse=True))
    return answer


# -------- 다른 풀이 ----------
# def solution(s):
#     answer = list(s)
#     answer.sort(reverse=True)

#     return ''.join(answer)


print(solution("Zbcdefg"))