from main import vectorGenerator as vg

arr = [1 for _ in range(23)]

for i in range(1, 5, 1):
    res = vg(arr, i)
    for j in range(2**i):
        print(res[j])
    print()
