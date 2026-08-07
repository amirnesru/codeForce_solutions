for i in range (int(input())):
    n,k = map(int, input().split())
    priceProduct = list(map(int, input().split()))
    valueDiscount = list(map(int, input().split()))
    sum1 = sum(priceProduct)
    curr_ind = -1
    valueDiscount.sort()
    priceProduct .sort(reverse=True)
    for i in range (k):
        curr_ind +=valueDiscount[i]
        if curr_ind >= n :
            break
        sum1 -= priceProduct[curr_ind]
    print(sum1)