fr = [-1] * 3

def display():
    for i in range(3):
        print(f"\t{fr[i]}", end="")
    print()

def main():
    p = [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2]
    fs = [0] * 3
    pf = 0
    frsize = 3
    for j in range(12):
        flag1 = 0
        flag2 = 0
        for i in range(3):
            if fr[i] == p[j]:
                flag1 = 1
                flag2 = 1
                break
        if flag1 == 0:
            for i in range(3):
                if fr[i] == -1:
                    fr[i] = p[j]
                    flag2 = 1
                    break
        if flag2 == 0:
            for i in range(3):
                fs[i] = 0
            for k in range(j + 1, 12):
                for i in range(3):
                    if fr[i] == p[k]:
                        fs[i] = 1
            for i in range(3):
                if fs[i] == 0:
                    index = i
                    break
            fr[index] = p[j]
            pf += 1
        display()
    print(f"\nno of page faults :{pf + frsize}")

main()
