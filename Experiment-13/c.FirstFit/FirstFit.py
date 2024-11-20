def first_fit_memory_management():
    max_blocks = 25
    frag = [0] * max_blocks
    b = [0] * max_blocks
    f = [0] * max_blocks
    bf = [0] * max_blocks
    ff = [0] * max_blocks

    print("\n\tMemory Management Scheme - First Fit")
    
    nb = int(input("Enter the number of blocks: "))
    nf = int(input("Enter the number of files: "))
    
    print("\nEnter the size of the blocks:-")
    for i in range(1, nb + 1):
        b[i] = int(input(f"Block {i}: "))
    
    print("\nEnter the size of the files :-")
    for i in range(1, nf + 1):
        f[i] = int(input(f"File {i}: "))
    
    for i in range(1, nf + 1):
        for j in range(1, nb + 1):
            if bf[j] != 1:
                temp = b[j] - f[i]
                if temp >= 0:
                    ff[i] = j
                    bf[j] = 1
                    frag[i] = temp
                    break
        else:
            ff[i] = -1
    
    print("\nFile_no:\tFile_size:\tBlock_no:\tBlock_size:\tFragement")
    for i in range(1, nf + 1):
        if ff[i] != -1:
            print(f"{i}\t\t{f[i]}\t\t{ff[i]}\t\t{b[ff[i]]}\t\t{frag[i]}")
        else:
            print(f"{i}\t\t{f[i]}\t\tNot Allocated\t\t\t\t\t\t")

if __name__ == "__main__":
    first_fit_memory_management()
