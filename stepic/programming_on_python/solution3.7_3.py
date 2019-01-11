s = set(input().lower() for i in range(int(input())))
print("\n".join(set(sum([input().lower().split() for i in range(int(input()))], [])) - s))
