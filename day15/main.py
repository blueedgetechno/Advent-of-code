from stack import PriorityQueue
from math import inf

with open('input.txt','r') as f:
    s = f.read().strip('\n')

s = s.split("\n")
a = []
for x in s:
    a += list(map(int,list(x))),

n = len(a)
sf = 5 # 1 for part 1
b = []
for i in range(sf * n):
    b += [0] * (sf * n),

for i in range(n):
    for j in range(n):
        for dx in range(sf):
            for dy in range(sf):
                v = a[i][j] - 1
                v += dx + dy
                v %= 9
                v += 1
                b[n * dx + i][n * dy + j] = v

n = len(b)
def isValid(i,j):
    return 0<=i<n and 0<=j<n

def fromId(id):
    return id//n,id%n

pq = PriorityQueue()
d = dict()
for i in range(n):
    for j in range(n):
        id = n*i + j
        ds = 0 if id==0 else inf
        d[id] = [0,ds,0]
        if id==0:
            pq.push(id,ds)

while not pq.isEmpty():
    v = pq.pop()
    x,y = fromId(v)
    for dx in range(-1,2):
        for dy in range(-1,2):
            nx = x+dx
            ny = y+dy
            if dx*dy==0 and dx!=dy and isValid(nx,ny):
                nv = n*nx + ny
                if d[nv][0]==1: continue
                mn = d[v][1] + b[nx][ny]
                if mn<d[nv][1]:
                    d[nv][1] = mn
                    pq.update(nv,mn)
                    d[nv][2] = v

    d[v][0] = 1

print(d[n*n - 1][1])
