st = {"север": 0, "юг": 0, "запад": 0, "восток": 0};
n = int(input());
for _ in range(n):
    i = input().split();
    st[i[0]] += int(i[1]);
print("{0} {1}".format(st["восток"] - st["запад"], st["север"] - st["юг"]));
