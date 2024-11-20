def best_fit_memory_management():
    max_blocks = 25
    frag = [0] * max_blocks
    b = [0] * max_blocks
    f = [0] * max_blocks
    bf = [0] * max_blocks
    ff = [0] * max_blocks
    lowest = 10000
    
    print("\nEnter the number of blocks:")
    nb = int(input())
    print("Enter the number of files:")
    nf = int(input())

    print("\nEnter the size of the blocks:-")
    for i in range(1, nb + 1):
        b[i] = int(input(f"Block {i}: "))

    print("Enter the size of the files :-")
    for i in range(1, nf + 1):
        f[i] = int(input(f"File {i}: "))

    for i in range(1, nf + 1):
        for j in range(1, nb + 1):
            if bf[j] != 1:
                temp = b[j] - f[i]
                if temp >= 0:
                    if lowest > temp:
                        ff[i] = j
                        lowest = temp
        frag[i] = lowest
        bf[ff[i]] = 1
        lowest = 10000

    print("\nFile No\tFile Size\tBlock No\tBlock Size\tFragment")
    for i in range(1, nf + 1):
        if ff[i] != 0:
            print(f"{i}\t\t{f[i]}\t\t{ff[i]}\t\t{b[ff[i]]}\t\t{frag[i]}")

if __name__ == "__main__":
    best_fit_memory_management()
