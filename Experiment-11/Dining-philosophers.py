# Dining Philosophers Problem in Python

def one():
    pos = 0
    for i in range(howhung):
        print(f"\nP {philname[hu[pos]]} is granted to eat")
        for x in range(pos, howhung):
            print(f"P {philname[hu[x]]} is waiting")
        pos += 1

def two():
    s = 0
    for i in range(howhung):
        for j in range(i + 1, howhung):
            if abs(hu[i] - hu[j]) >= 1 and abs(hu[i] - hu[j]) != 4:
                print(f"\n\nCombination {s + 1}")
                t = hu[i]
                r = hu[j]
                s += 1
                print(f"P {philname[hu[i]]} and P {philname[hu[j]]} are granted to eat")
                for x in range(howhung):
                    if hu[x] != t and hu[x] != r:
                        print(f"P {philname[hu[x]]} is waiting")

def main():
    global tph, philname, status, howhung, hu, cho
    print("\n\nDINING PHILOSOPHER PROBLEM")

    tph = int(input("Enter the total no. of philosophers: "))
    
    philname = [i + 1 for i in range(tph)]
    status = [1 for _ in range(tph)]

    howhung = int(input("How many are hungry: "))
    
    if howhung == tph:
        print("\nAll are hungry..\nDead lock stage will occur")
        print("Exiting\n")
        return
    
    hu = []
    for i in range(howhung):
        pos = int(input(f"Enter philosopher {i + 1} position: "))
        hu.append(pos)
        status[pos] = 2
    
    while True:
        print("1. One can eat at a time")
        print("2. Two can eat at a time")
        print("3. Exit")
        
        cho = int(input("Enter your choice: "))
        
        if cho == 1:
            one()
        elif cho == 2:
            two()
        elif cho == 3:
            print("Exiting")
            break
        else:
            print("\nInvalid option..")

if __name__ == "__main__":
    main()
