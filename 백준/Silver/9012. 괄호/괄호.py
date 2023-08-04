num = int(input())
for n in range(num):
    ps = input()
    ps_list = list()
    
    for c in ps:
        if c == "(":
            ps_list.append(c)
        elif c== ")":
            if ps_list:
                ps_list.pop()
            else:
                print("NO")
                break
    else:
        if ps_list:
            print("NO")
        else:
            print("YES")