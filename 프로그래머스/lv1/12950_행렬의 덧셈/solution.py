# ----------- 내 풀이 -----------
def solution(arr1, arr2):
    answer = list()

    for a1, a2 in zip(arr1, arr2):
        answer.append([n1 + n2 for n1, n2 in zip(a1, a2)])

    return answer


# ----------- 다른 풀이 -----------
# def solution(arr1, arr2):
#     answer = [[n1 + n2 for n1, n2 in zip(a1, b2)] for a1, b2 in zip(arr1, arr2)]
#     return answer


# def solution(arr1, arr2):
#     for i in range(len(arr1)):  # 행
#         for j in range(len(arr1[0])):  # 열
#             arr1[i][j] += arr2[i][j]

#     return arr1


# def solution(arr1, arr2):
#     answer = list()
#     for i in range(len(arr1)):  # 행
#         arr = list()
        
#         for j in range(len(arr1[0])):  # 열
#             arr.append(arr1[i][j] + arr2[i][j])
            
#         answer.append(arr)

#     return answer


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
print(solution([[1], [2]], [[3], [4]]))
