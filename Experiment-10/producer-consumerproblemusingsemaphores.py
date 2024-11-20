def main():
    buffer = [0] * 10  # Initialize buffer with 10 elements
    bufsize = 10
    in_index = 0
    out_index = 0
    choice = 0
    
    while choice != 3:
        print("\n1. Produce \t 2. Consume \t 3. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            if (in_index + 1) % bufsize == out_index:
                print("\nBuffer is Full")
            else:
                produce = int(input("\nEnter the value: "))
                buffer[in_index] = produce
                in_index = (in_index + 1) % bufsize
                
        elif choice == 2:
            if in_index == out_index:
                print("\nBuffer is Empty")
            else:
                consume = buffer[out_index]
                print(f"\nThe consumed value is {consume}")
                out_index = (out_index + 1) % bufsize
        
        elif choice == 3:
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
