with open('input.txt', 'r') as f: s = f.read().strip('\n')

s = s.split()
symb = ["[",",","]"]
s = [list(x) for x in s]
a = []
for x in s:
    a+=[],
    for y in x:
        if y not in symb: a[-1]+=int(y),
        else: a[-1]+=y,

def explode(c):
    d = []
    l = len(c)
    i = 0
    j = -1
    z = 0
    td = 0
    while i<l:
        x = c[i]
        if x not in symb: j = i
        if x == "[": z+=1
        if x == "]": z-=1
        if z==5:
            if j+1>0:
                d[j]+=c[i+1]

            d+=0,
            td = c[i+3]
            i+=5
            break

        d+=x,
        i+=1

    while i<l:
        x = c[i]
        if x not in symb and td:
            x += td
            td = 0

        d+=x,
        i+=1

    return d,len(d)!=len(c)

def split(c):
    d = []
    l = len(c)
    i = 0
    z = 1
    while i<l:
        x = c[i]
        if x not in symb and x>9 and z:
            d+="[",
            d+=x//2,
            d+=",",
            d+=(x+1)//2,
            d+="]",
            z=0
            i+=1
            continue

        d+=x,
        i+=1

    return d,len(d)!=len(c)

def reduce(c):
    d = 0
    z = 1
    while z>0:
        z = 2
        c,d = explode(c)
        z-=int(not d)
        if not d:
            c,d = split(c)
            z-=int(not d)

    return c

def mag(c):
    l = len(c)
    if l==1: return c[0]
    i = 1
    z = 0
    d = [[]]
    while i<l-1:
        x = c[i]
        if x == "[": z+=1
        if x == "]": z-=1
        if z==0 and x==",":
            d+=[],
        else:
            d[-1]+=x,

        i+=1

    return 3*mag(d[0]) + 2*mag(d[1])

def add(b1,b2):
    b = ["["]+b1+[","]+b2+["]"]
    return reduce(b)

def part1():
    b = a[0]
    for x in a[1:]:
        b = add(b,x)

    print(mag(b))

def part2():
    i = 0
    l = len(a)
    ans2 = 0
    while i<l-1:
        print(i)
        j = i+1
        while j<l:
            mg1 = mag(add(a[i],a[j]))
            mg2 = mag(add(a[j],a[i]))
            ans2 = max(ans2, max(mg1,mg2))
            j+=1
        i+=1

    print(ans2)

# part1()
part2()
