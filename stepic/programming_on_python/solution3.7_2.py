a, b, c, d = input(), input(), input(), input()
print('{}\n{}'.format(''.join(b[a.index(i)] for i in c), ''.join(a[b.index(i)] for i in d)))
