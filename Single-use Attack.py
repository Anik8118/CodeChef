# cook your dish here
for _ in range(int(input())):
	h, x, y = map(int, input().split())
	print(1 + (h-y+x-1)//x)