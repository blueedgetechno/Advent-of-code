with open('input.txt', 'r') as f: s = f.read().strip('\n')

s = s.split("\n\n")
alg = s[0]
a = s[1].split("\n")
a = [list(x) for x in a]
n = len(a)

m = 201
b = []
for i in range(m):
    b+=[],
    for j in range(m):
        b[-1]+=0,

x,y = m//2,m//2
x-=n//2
y-=n//2


for i in range(n):
    for j in range(n):
        b[x+i][y+j] = int(a[i][j]=="#")

pr = int(alg[0]=="#")

def isValid(i,j):
    return 0<=i<m and 0<=j<m

t = 0
while t<50:
    print(t)
    c = []
    for i in range(m):
        c+=[],
        for j in range(m):
            id = 0
            for dx in range(-1,2):
                for dy in range(-1,2):
                    id*=2
                    if isValid(i+dx,j+dy):
                        id+=b[i+dx][j+dy]
                    else:
                        id += (t%2)*pr

            c[-1]+=int(alg[id]=="#"),

    b = c
    t+=1

ans = 0
for x in b:
    ans+=sum(x)

print(ans)
