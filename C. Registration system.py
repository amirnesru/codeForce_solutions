n = int(input())
count = {}

for _ in range(n):
    req = input()
    if req in count:
        print(req + str(count[req]))
        count[req] += 1
    else:
        print("OK")
        count[req] = 1
