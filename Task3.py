# n = int(input('Введите число n'))
# p=1
# while p<=n:
#     print(p)
#     p=p*2

input()
lst = map(int, (input().split()))
n = int(input())
inc = 0
for i in lst:
    if i == n:
        inc += 1
print(inc)