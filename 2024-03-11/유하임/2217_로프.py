import sys
N = int(sys.stdin.readline().strip())
array, result = [], []
for _ in range(N):
    array.append(int(sys.stdin.readline().strip()))
array.sort()
for i in array:
    result.append(N * i)
    N -= 1
print(max(result))