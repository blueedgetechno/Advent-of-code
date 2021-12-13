with open('input.txt','r') as f:
    s = f.read().strip('\n')

s = s.split("\n\n")
dots = s[0].strip().split("\n")
dots = list(map(lambda x: x.split(","), dots))
folds = s[1].strip().split("\n")
folds = list(map(lambda x: x.strip("fold along").split("="), folds))
a = []
mr = 0
mc = 0
for y,x in dots:
    mr = max(mr, int(x))
    mc = max(mc, int(y))

for i in range(mr+1):
    a+=[],
    for j in range(mc+1):
        a[-1]+=0,

for y,x in dots:
    a[int(x)][int(y)] = 1

for f in folds:
    c = int(f[1])
    n = len(a)
    m = len(a[0])
    b = []
    nb = n
    mb = m
    if f[0]=="y": nb = c
    if f[0]=="x": mb = c

    # print(nb,mb)

    for i in range(nb):
        b+=[0]*mb,
        for j in range(mb):
            b[i][j]=a[i][j]

            ri = i
            rj = j
            if f[0]=="y": ri = 2*c - i
            if f[0]=="x": rj = 2*c - j

            if 0<=ri<n and 0<=rj<m:
                b[i][j]|=a[ri][rj]

    a = []
    for x in b:
        a+=x[:],


ans1 = 0
for x in a:
    ans1+=sum(x)

# print(ans1)

for i in range(len(a)):
    for j in range(len(a[0])):
        a[i][j] = " " if a[i][j]==0 else "*"

for x in a:
    print(*x)
