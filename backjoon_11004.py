import sys
input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort()

print('\n'.join(f'{x} {y}' for x, y in arr))