# ---------- 내 풀이 --------------
def solution(absolutes, signs):
    answer = 0

    for i in range(len(signs)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer


# ---------- 다른 풀이 --------------
# def solution(absolutes, signs):
#     answer = 0

#     # zip()
#     # 여러 개의 반복 가능한 객체를 받아서, 해당 객체들로부터 각 항목들을 순서대로 묶어 튜플로 반환하는 함수
#     for absolute, sign in zip(absolutes, signs):
#         if sign:
#             answer += absolute
#         else:
#             answer -= absolute

#     return answer


# def solution(absolutes, signs):
#     answer = sum(absolute if sign else -absolute for absolute, sign in zip(absolutes, signs))
#     return answer


print(solution([4, 7, 12], [True, False, True]))
print(solution([1, 2, 3], [False, False, True]))
