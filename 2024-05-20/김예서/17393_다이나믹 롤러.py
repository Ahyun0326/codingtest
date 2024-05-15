import sys
input = sys.stdin.readline

'''
이분탐색

자신보다 작은 값들 중 최대값의 위치 찾기
'''

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(n):

    result = i
    start = i+1
    end = n-1

    while (start <= end):
        mid = (start+end)//2
        # 현재 잉크보다 점도가 클 경우
        if a[i] < b[mid]:
            end = mid-1
        # 현재 잉크보다 점도가 작거나 같을 경우
        elif a[i] >= b[mid]:
            start = mid+1
            result = mid
    
    print(result-i, end=' ')