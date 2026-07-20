for i in range(int(input())):
    hour,minu = map(int, input().split())
    print((23-hour)*60 + 60-minu)