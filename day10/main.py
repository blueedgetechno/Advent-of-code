with open('input.txt','r') as f:
    s = f.read().strip('\n')

a = s.split("\n")

p = {"(":")","[":"]","{":"}","<":">"}
op = ["(","[","{","<"]
cl = [")","]","}",">"]
sc = {")": 3,"]":57,"}":1197,">":25137}

def check(s):
    st = []
    for x in s:
        if x in op:
            st+=p[x],
        else:
            if len(st)>0 and st[-1]==x:
                st.pop()
            else:
                return [-1, x]

    return [0, "".join(st[::-1])]

def score(s):
    t = 0
    for x in s:
        t*=5
        t+=cl.index(x)+1

    return t

ans1 = 0
ans2 = []
for s in a:
    ch = check(s)
    if ch[0]==-1:
        ans1+=sc[ch[1]]
    else:
        ans2+=score(ch[1]),

# print(ans1)
ans2.sort()
ans2=ans2[len(ans2)//2]
print(ans2)
