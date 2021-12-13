with open('input.txt','r') as f:
    s = f.read().strip('\n')

a = s.split("\n")
a = [x.split("|") for x in a]

d = dict()
d["abcefg"] = 0  # 6
d["cf"] = 1      # 2
d["acdeg"] = 2   # 5
d["acdfg"] = 3   # 5
d["bcdf"] = 4    # 4
d["abdfg"] = 5   # 5
d["abdefg"] = 6  # 6
d["acf"] = 7     # 3
d["abcdefg"] = 8 # 7
d["abcdfg"] = 9  # 6

b = []
for y in a:
    b+=[x.strip().split() for x in y],

def flat(s1): return "".join(sorted(list(set(s1))))
def same(s1,s2): return flat(s1)==flat(s2)
def add(s1,s2):
    s1 = set(s1)
    s2 = set(s2)
    return "".join(s2.union(s1))

def common(s1,s2):
    s1 = set(s1)
    s2 = set(s2)
    return "".join(s2.intersection(s1))

def subtract(s1,s2="abcdefg"):
    s1 = set(s1)
    s2 = set(s2)
    return "".join(s2.difference(s1))

def solve(p):
    d1 = dict()
    n = dict()
    m = dict()
    for x in p:
        d1[len(x)]=d1.get(len(x), [])
        d1[len(x)]+=x,
    n[1] = d1[2][0]
    n[7] = d1[3][0]
    n[4] = d1[4][0]
    n[8] = d1[7][0]

    m['a'] = subtract(n[1],n[7])
    for x in d1[5]:
        if same(add(x,n[1]), x): n[3] = x
        if same(add(x,n[4]), n[8]): n[2] = x

    m['b'] = subtract(n[3],n[4])
    m['d'] = subtract(n[1],common(n[3],n[4]))
    m['e'] = subtract(add(n[3],n[4]))
    m['g'] = subtract(add(n[4],n[7]), add(n[4],n[3]))
    m['c'] = common(n[1],n[2])
    m['f'] = subtract(n[2],n[3])

    return {v: k for k, v in m.items()}

def decode(a,m):
    a1 = []
    for x in a:
        x = [m[y] for y in x]
        x = flat("".join(x))
        a1+=d[x],
    return "".join([str(x) for x in a1])

ans1 = 0
ans2 = 0

for x in b:
    mp = solve(x[0])
    v = decode(x[1],mp)
    for x in v:
        if x in ['1','4','7','8']: ans1+=1
    ans2+=int(v)

print(ans1)
print(ans2)
