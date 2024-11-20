def main():
    n = int(input("Enter the number of tracks to be traversed: "))
    h = int(input("Enter the position of the head: "))
    t = [0, h]
    
    print("Enter the tracks:")
    for _ in range(n):
        t.append(int(input()))
    
    t.sort()
    head_index = t.index(h)
    
    atr = []
    for i in range(head_index, -1, -1):
        atr.append(t[i])
    for i in range(head_index + 1, len(t)):
        atr.append(t[i])
    
    sum_movements = 0
    for i in range(len(atr) - 1):
        sum_movements += abs(atr[i] - atr[i + 1])
    
    average_movements = sum_movements / n
    
    print("\nOrder of tracks accessed:")
    print(" -> ".join(map(str, atr)))
    print(f"\nTotal Head Movements: {sum_movements}")
    print(f"Average Head Movements: {average_movements:.2f}")


if __name__ == "__main__":
    main()
