d = {}
for a, p, b, v in (input().split(';') for n in range(int(input()))):
    d[a] = [i + j for i, j in
            zip(d.setdefault(a, [0, 0, 0, 0, 0]), [1, (p > v), (p == v), (p < v), 3 if p > v else (p == v)])]
    d[b] = [i + j for i, j in
            zip(d.setdefault(b, [0, 0, 0, 0, 0]), [1, (p < v), (p == v), (p > v), 3 if p < v else (p == v)])]
print(*(i + ":" + ' '.join(map(str, d.get(i))) for i in d), sep='\n')
