a, b = map(int, input().strip().split(" "))     # 입력

# ---------- 내 풀이 ----------
for i in range(b):
    for j in range(a):
        print("*", end="")
    print()


# --------- 다른 풀이 ----------
# for _ in range(b):
#     print("*"*a)


# answer = ("*" * a + "\n") * b
# print(answer)
