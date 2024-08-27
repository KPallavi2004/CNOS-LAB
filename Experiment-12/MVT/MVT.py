def main():
    # Input the total memory available
    ms = int(input("\nEnter the total memory available (in Bytes)-- "))
    temp = ms
    mp = []
    n = 0
    ch = 'y'
    
    while ch == 'y':
        # Input memory required for each process
        mem_req = int(input(f"\nEnter memory required for process {n+1} (in Bytes) -- "))
        mp.append(mem_req)

        if mem_req <= temp:
            print(f"\nMemory is allocated for Process {n+1}")
            temp -= mem_req
            n += 1
        else:
            print("\nMemory is Full")
            break

        # Ask if the user wants to continue
        ch = input("\nDo you want to continue(y/n) -- ").strip()

    # Display results
    print(f"\n\nTotal Memory Available -- {ms}")
    print("\n\tPROCESS\t\t MEMORY ALLOCATED ")
    for i in range(n):
        print(f"\n \t{i+1}\t\t{mp[i]}")

    print(f"\n\nTotal Memory Allocated is {ms-temp}")
    print(f"Total External Fragmentation is {temp}")

if __name__ == "__main__":
    main()
