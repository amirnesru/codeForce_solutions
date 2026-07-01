for i in range (int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    possible = True
    for i in range(1, n - 1, 2):
        if nums[i] != nums[i + 1]:
            possible = False
            break

    print("YES" if possible else "NO")