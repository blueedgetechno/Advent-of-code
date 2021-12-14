with open('input.txt','r') as f:
    s = f.read().strip('\n')

s = s.split("\n\n")
a = s[0].strip()
b = s[1].strip().split("\n")
b = list(map(lambda x: x.split(" -> "), b))

d = dict()
dp = dict()
for x,y in b: d[x] = y

for i in range(len(a)-1):
    x = a[i]+a[i+1]
    dp[x] = dp.get(x,0)
    dp[x] += 1

st = 10
while st>0:
    c = dp.copy()

    for x in dp:
        px = x[0]+d[x]
        xn = d[x]+x[1]
        c[x]-=dp[x]
        c[px] = c.get(px,0)
        c[px]+= dp[x]
        c[xn] = c.get(xn,0)
        c[xn]+= dp[x]

    dp = c.copy()
    st-=1

f = dict()
for x in dp:
    f[x[0]] = f.get(x[0],0)
    f[x[1]] = f.get(x[1],0)
    f[x[0]]+=dp[x]
    f[x[1]]+=dp[x]

f[a[0]]+=1
f[a[len(a)-1]]+=1

fr = sorted(f.values())
ans1 = (fr[-1] - fr[0])//2
print(ans1)
