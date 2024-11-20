def display(fr, m):
    for i in range(m):
        print(f"{fr[i]}\t", end="")
    print()

def main():
    n = int(input("Enter length of the reference string: "))
    page = [int(input()) for _ in range(n)]
    m = int(input("Enter number of frames: "))
    
    fr = [-1] * m
    pf = m
    for i in range(m):
        fr[i] = -1
    
    for j in range(n):
        flag1 = flag2 = 0
        
        for i in range(m):
            if fr[i] == page[j]:
                flag1 = 1
                flag2 = 1
                break
        
        if flag1 == 0:
            for i in range(m):
                if fr[i] == -1:
                    fr[i] = page[j]
                    flag2 = 1
                    break
        
        if flag2 == 0:
            lg = [0] * m
            for i in range(m):
                for k in range(j + 1, n):
                    if fr[i] == page[k]:
                        lg[i] = k - j
                        break
            
            found = 0
            for i in range(m):
                if lg[i] == 0:
                    index = i
                    found = 1
                    break
            
            if found == 0:
                max_val = lg[0]
                index = 0
                for i in range(m):
                    if max_val < lg[i]:
                        max_val = lg[i]
                        index = i
            
            fr[index] = page[j]
            pf += 1
        
        display(fr, m)
    
    print(f"Number of page faults: {pf}")
    pr = (pf / n) * 100
    print(f"Page fault rate = {pr:.2f}%")

main()
