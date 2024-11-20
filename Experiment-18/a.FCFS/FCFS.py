def main():
    # Input the number of tracks
    n = int(input("Enter the number of tracks: "))

    # Input the tracks to be traversed
    t = []
    print("Enter the tracks to be traversed:")
    for i in range(n):
        t.append(int(input()))

    # Calculate the absolute differences between consecutive tracks
    tohm = []
    for i in range(1, n):
        difference = abs(t[i] - t[i - 1])
        tohm.append(difference)

    # Calculate total head movements and average head movements
    tot = sum(tohm)
    avhm = tot / n

    # Display results
    print("\nTracks Traversed\tDifference Between Tracks")
    for i in range(len(tohm)):
        print(f"{t[i]} -> {t[i + 1]}\t\t\t{tohm[i]}")

    print(f"\nTotal Header Movements: {tot}")
    print(f"Average Header Movements: {avhm:.2f}")


if __name__ == "__main__":
    main()
