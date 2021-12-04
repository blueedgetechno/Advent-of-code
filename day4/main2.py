with open('input.txt','r') as f:
    s = f.read()

s = s.strip('\n')
s = s.split('\n\n')

q = s[0]
b0 = s[1:]

q = [int(x) for x in q.split(',')]
b = []

for x in b0:
    y = [z for z in x.split('\n')]
    c = []
    for z in y:
        c+=[int(k) for k in z.split(' ') if len(k)!=0],

    b+=c,

# same sh*t

def mark(i,a):
    for j in range(5):
        for k in range(5):
            if b[i][j][k]==a:
                b[i][j][k]=-1
                break

def check(i):
    rw = [0,0,0,0,0]
    cl = [0,0,0,0,0]
    for j in range(5):
        for k in range(5):
            rw[j]+=b[i][j][k]
            cl[k]+=b[i][j][k]

    for x in rw:
        if x==-5: return True

    for x in cl:
        if x==-5: return True

    return False

def sumMat(i):
    sm = 0
    for j in range(5):
        for k in range(5):
            if b[i][j][k]!=-1:
                sm+=b[i][j][k]

    return sm

bl = len(b)
bz = [True]*bl # this will track if the board has already wwon
ans = 0
res = bl # counts the remaining number of boards that left to be won
for a in q:
    if res<1: break # breaks as soon as every board has won

    for i in range(bl):
        mark(i,a)

        if check(i) and bz[i]:
            sm = sumMat(i)
            ans = a*sm
            res-=1
            bz[i]=False # marking the winning of the board

print(ans)
