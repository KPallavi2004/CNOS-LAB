def display(fr):
    print("\t".join(map(str, fr)))

def main():
    fr = [-1, -1, -1]
    page = [2, 3, 2, 1, 5, 2, 4, 5, 3, 4, 6, 9]
    frsize = 3
    top = 0
    pf = 0

    for j in range(len(page)):
        flag1 = 0
        flag2 = 0
        
        for i in range(frsize):
            if fr[i] == page[j]:
                flag1 = 1
                flag2 = 1
                break
        
        if flag1 == 0:
            for i in range(frsize):
                if fr[i] == -1:
                    fr[i] = page[j]
                    flag2 = 1
                    break
        
        if flag2 == 0:
            fr[top] = page[j]
            top += 1
            pf += 1
            if top >= frsize:
                top = 0
        
        display(fr)
    
    print(f"Number of page faults: {pf + frsize}")

if __name__ == "__main__":
    main()
