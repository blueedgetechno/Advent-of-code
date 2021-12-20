with open('input.txt', 'r') as f: s = f.read().strip('\n')

s = s.split("\n\n")
alg = s[0]
a = s[1].split("\n")
a = [list(x) for x in a]

def clean(b):
    m = len(b)
    c = []
    for i in range(m):
        c+=[],
        for j in range(m):
            c[-1]+=str(int(b[i][j]=="#")),
        if m%2==0:
            c[-1]+="0",

    if m%2==0:
        c+=["0"]*(m+1),

    return c

def unwrap(b):
    n = len(b)
    c = ""
    for i in range(n*n):
        x,y = pos(i)
        x+=n//2
        y+=n//2
        c += b[x][y]

    return c

def f(n):
    d = n*0.25 + 0.125
    d**=0.5
    d-=0.25
    return int(d)

def sign(x):
    if x==0: return 0
    if x>0: return 1
    return -1

def normal(dv):
    return [sign(dv[0]),sign(dv[1])]

def pos(n):
    k = f(n)
    p = [k, -k]
    t = (2*k - 1)*(2*k + 1)
    dr = [[-1,0],[0,1],[1,0],[0,-1]]
    stp = 2*k + 1

    for dxy in dr:
        t += stp
        stp = 2*k + 1 + int(dxy==[1,0])
        d = n - t
        if d<=stp:
            p[0] += dxy[0]*d
            p[1] += dxy[1]*d
            return p

        p[0] += dxy[0]*stp
        p[1] += dxy[1]*stp

def invpos(x,y):
    k = max(abs(x),abs(y))
    if y==-k: k+=1
    k -= 1

    v = 2*k*(2*k + 1)
    if x==k and y==-k: return v

    p = [k, -k]
    dr = [[-1,0],[0,1],[1,0],[0,-1]]
    stp = 0
    for dxy in dr:
        stp = 2*k + 1 + int(dxy==[1,0])
        dv = [x-p[0],y-p[1]]

        if normal(dv)==dxy:
            df = max(abs(dv[0]),abs(dv[1]))
            v += df
            return v

        v += stp
        p[0] += dxy[0]*stp
        p[1] += dxy[1]*stp

def padd(b,t):
    n = len(b)
    n = round(n**0.5)
    b += str((t%2)*int(alg[0]=="#"))*(4*(n+1))
    return b

def enhance(b,t):
    l = len(b)
    c = ""
    for i in range(l):
        x,y = pos(i)

        id = 0
        for dx in range(-1,2):
            for dy in range(-1,2):
                v = invpos(x+dx,y+dy)
                id*=2
                if v<l:
                    id+=int(b[v])
                else:
                    id+=(t%2)*int(alg[0]=="#")

        c+=str(int(alg[id]=="#"))

    return c

def light(b):
    return b.count("1")

def show(b):
    n = len(b)
    n = round(n**0.5)
    n//=2
    for i in range(-n,n+1):
        for j in range(-n,n+1):
            v = invpos(i,j)
            print("#" if b[v]=="1" else ".",end="")
        print()

    print()

a = clean(a)
a = unwrap(a)
# show(a)

t = 0
while t<2: #50 for part2
    print(t)
    a = padd(a,t)
    a = enhance(a,t)
    t+=1
    # show(a)

ans1 = light(a)

print(ans1)
