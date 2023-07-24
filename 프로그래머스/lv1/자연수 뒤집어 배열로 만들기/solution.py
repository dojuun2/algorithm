# ---------- 내 풀이 ------------
def solution(n):
    answer = [int(i) for i in str(n)]
    answer.reverse()
    return answer

# ----------- 다른 풀이 -----------
# def solution(n):
#     # map()
#     # 기존 리스트나 시퀀스의 각 요소에 동일한 함수를 적용하여 새로운 리스트를 생성하는 함수
#     # 이를 통해 반복문 없이 간단하게 데이터 변환이 가능하다
#     answer = list(map(int, reversed(str(n))))
    
#     return answer

# def solution(n):
#     # [::-1]
#     # 리스트 슬라이싱 기법 중 하나
#     # 리스트의 요소들을 역순으로 가져오는 방법
#     #   - 시작: 생략되었으므로 리스트의 시작 위치를 가리킵니다.
#     #   - 끝: 생략되었으므로 리스트의 끝 위치를 가리킵니다.
#     #   - 간격: -1이므로 리스트를 역순으로 가져옵니다.
#     answer = [int(i) for i in str(n)][::-1]
#     print(answer)
#     return answer

solution(12345)