with open('input.txt','r') as f:
    s = f.read().strip('\n')

a = []
b = []
for st in s.split("\n"):
    a+=[],
    b+=[],
    for x in st:
        a[-1]+=int(x),
        b[-1]+=0,

n = len(a)
m = len(a[0])
def isValid(i,j):
    return 0<=i<n and 0<=j<m

d = [[0,1],[0,-1],[1,0],[-1,0]]
def isLowest(i,j):
    res = True
    for dx,dy in d:
        if isValid(i+dx,j+dy):
            res&=a[i+dx][j+dy]>a[i][j]

    return res

def go(i,j,nm):
    b[i][j]=nm

    for dx,dy in d:
        if isValid(i+dx,j+dy):
            if b[i+dx][j+dy]==0:
                if a[i+dx][j+dy]<9 and a[i+dx][j+dy]>=a[i][j]:
                    go(i+dx,j+dy,nm)

c = 0
ans1 = 0
for i in range(n):
    for j in range(m):
        if isLowest(i,j):
            c+=1
            ans1 += a[i][j]+1
            go(i,j,c)

# print(ans1)

d = dict()
for x in b:
    for y in x:
        if y>0:
            d[y] = d.get(y,0)
            d[y] += 1

ans2 = sorted(list(d.values()),reverse=True)[:3]
ans2 = ans2[0]*ans2[1]*ans2[2]
print(ans2)
