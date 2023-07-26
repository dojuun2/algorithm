# ------------- 내 풀이 ------------
# def solution(s):
#     answer = ""

#     index = len(s) // 2
#     if len(s) % 2:
#         answer += s[index]
#     else:
#         answer += s[index - 1 : index + 1]

#     return answer


# ------------- 다른 풀이 ------------
def solution(s):
    # 인덱스는 항상 0 번째부터 출발하니까, 문자열 길이 len()에서 1을 빼고 //2를 한다면 짝수는 자연스럽게 1이 하나 더 뺀 값이 나온다.
    # (len(s) - 1) // 2
    
    # 문자열 길이: 4
        # 여기서 1을 뺀 값 3에서 //2를 하면 =====> 1이 나온다....
    # 문자열 길이: 5
        # 여기서 1을 뺀 값 4에서 //2를 하면 =====> 2가 나온다....
    # 얘를 슬라이싱의 앞 인덱스로 사용하면 짝수, 홀수를 신경쓰지 않아도 됨


    answer = s[(len(s) - 1) // 2 : len(s) // 2 + 1]
    # "abcde" 일 때 => 길이 5
        # s[(len(s) - 1) // 2 : len(s) // 2 + 1]
        # => s[2:3]
        # => 인덱스 2에 해당하는 문자 출력
        # => c
    
    # "qwer" => 길이 4
        # s[(len(s) - 1) // 2 : len(s) // 2 + 1]
        # => s[1:3]
        # => 인덱스 1, 2에 해당하는 문자 출력
        # => we
    return answer


print(solution("abcde"))
print(solution("qwer"))
