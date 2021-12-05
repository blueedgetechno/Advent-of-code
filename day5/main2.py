with open('input.txt','r') as f:
    s = f.read()

s = s.strip('\n')
s = s.split('\n')

a = []
for x in s:
    p1,p2 = x.split("->")
    p1 = list(map(int, p1.strip().split(",")))[::-1]
    p2 = list(map(int, p2.strip().split(",")))[::-1]
    a+=[p1,p2],

bl = 1000
b = []
for i in range(bl):
    b+=[],
    for j in range(bl):
        b[i]+=[0,0,0,0],

def sortIt(p1,p2):
    if p1[0]<p2[0] or (p1[0]==p2[0] and p1[1]<p2[1]):
        return [p1,p2]
    else:
        return [p2,p1]

def poss(x,y): return -1<x<bl and -1<y<bl
def sign(x): return 0 if x==0 else [-1,1][int(x>0)]

d = [[0,1],[1,0],[1,1],[1,-1]] # expanding the hirizon

for x in a:
    p1,p2 = x
    for i,dr in enumerate(d):
        p1,p2 = sortIt(p1,p2)
        dx = [sign(p2[0]-p1[0]), sign(p2[1]-p1[1])]
        if dx[0]==dr[0] and dx[1]==dr[1]:
            b[p1[0]][p1[1]][i]+=1
            if poss(p2[0]+dr[0],p2[1]+dr[1]):
                b[p2[0]+dr[0]][p2[1]+dr[1]][i]-=1
            break

for i in range(bl):
    for j in range(bl):
        for k,dr in enumerate(d):
            if poss(i-dr[0],j-dr[1]):
                b[i][j][k]+=b[i-dr[0]][j-dr[1]][k]

ans = 0
for i in range(bl):
    for j in range(bl):
        b[i][j]=sum(b[i][j])
        if b[i][j]>1:
            ans+=1

print(ans)
