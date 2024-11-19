def main():
    n = int(input("Enter the number of tracks to be traversed: "))
    h = int(input("Enter the position of the head: "))
    t = [0, h]
    tot = int(input("Enter the total number of tracks: "))
    t.append(tot - 1)

    print("Enter the tracks:")
    for _ in range(n):
        t.append(int(input()))
    
    t.sort()
    head_index = t.index(h)
    atr = []
    p = 0

    while t[head_index] != tot - 1:
        atr.append(t[head_index])
        head_index += 1
        p += 1

    atr.append(t[head_index])
    p += 1
    i = 0

    while p != len(t) and t[i] != h:
        atr.append(t[i])
        i += 1
        p += 1

    sum_movements = 0
    for j in range(len(atr) - 1):
        sum_movements += abs(atr[j] - atr[j + 1])

    average_movements = sum_movements / n

    print(f"Total Head Movements: {sum_movements}")
    print(f"Average Head Movements: {average_movements:.2f}")


if __name__ == "__main__":
    main()
