from math import ceil, floor

with open('input.txt', 'r') as f: s = f.read().strip('\n')

a = s.strip("target area:").split(",")
tx = a[0].split("=")[1].split("..")
ty = a[1].split("=")[1].split("..")
tx = list(map(int, tx))
ty = list(map(int, ty))

def f(n, a0=1, d=1):
    return (n*(2*a0 + (n-1)*d))//2

def px(u,t):
    sg = 1 if u>0 else -1
    u = abs(u)
    psx = f(u) if t>u-1 else f(t,u,-1)
    return sg*psx

def py(v,t):
    return f(t,v,-1)

def inTarget(u,v,t):
    return tx[0]<=px(u,t)<=tx[1] and ty[0]<=py(v,t)<=ty[1]

rpx = []
for ux in tx:
    lx = 8*ux + 1
    lx**=0.5
    lx-=1
    lx/=2
    rpx+=lx,

rpx[0] = ceil(rpx[0])
rpx[1] = floor(rpx[1])

ans1 = 0
st = set()

for u in range(rpx[0], rpx[1]+1):
    t = u
    c = 0
    while True:
        rpy = []
        for y in ty:
            rpy += y/t + (t-1)/2,
        rpy[0] = ceil(rpy[0])
        rpy[1] = floor(rpy[1])
        if rpy[0]<=rpy[1]:
            for v in range(rpy[0],rpy[1]+1):
                if inTarget(u,v,t):
                    ans1 = max(ans1, f(v))
                    st.add(u + v*tx[1])

        else:
            c+=1
            if c>1000: break

        t+=1

u2 = 1
while u2<tx[1]+1:
    u1 = u2 - 1
    while (f(u2)-f(u1))<tx[1]+1 and u1>0:
        t = u2 - u1
        rpy = []
        for y in ty:
            rpy += y/t + (t-1)/2,

        rpy[0] = ceil(rpy[0])
        rpy[1] = floor(rpy[1])
        if rpy[0]<=rpy[1]:
            for v in range(rpy[0],rpy[1]+1):
                if inTarget(u2,v,t):
                    ans1 = max(ans1, f(v))
                    st.add(u2 + v*tx[1])

        u1-=1

    u2+=1

ans2 = len(st)
print(ans1) # part 1
print(ans2) # part 2
