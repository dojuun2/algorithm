# --------- 내 풀이 -----------
# def solution(phone_number):
#     answer = ''

#     for i in range(len(phone_number) - 1, -1, -1):
#         if i < len(phone_number) - 4:
#             answer += '*'
#         else:
#             answer += phone_number[i]

#     answer = list(answer)
#     answer.reverse()
#     return ''.join(answer)


# ---------- 다른 풀이 ------------
def solution(phone_number):
    # phone_number[-4:]
    # 슬라이싱
    # 끝에서 4번째 문자부터 끝까지 출력
    # 01033334444 => 4444
    answer = "*" * (len(phone_number) - 4) + phone_number[-4:]

    return answer


print(solution("01033334444"))
print(solution("027778888"))
