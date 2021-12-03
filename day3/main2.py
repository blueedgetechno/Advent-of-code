with open('input.txt','r') as f:
    s = f.read()

s = s.strip('\n')
s = s.split('\n')


i = 0
s1 = set(s)
while len(s1)>1 and i<12:
    z = 0
    ch = ""
    s2 = set()
    for x in s1: z+=2*int(x[i]) - 1

    if z>=0: ch="1"
    else: ch="0"

    for x in s1:
        if x[i]==ch: s2.add(x)

    s1 = set(s2)
    i+=1

ogr = list(s1)[0]

i = 0
s1 = set(s)
while len(s1)>1 and i<12:
    z = 0
    ch = ""
    s2 = set()
    for x in s1: z+=2*int(x[i]) - 1

    if z>=0: ch="0"
    else: ch="1"

    for x in s1:
        if x[i]==ch: s2.add(x)

    s1 = set(s2)
    i+=1

csr = list(s1)[0]

print(int(ogr,2)*int(csr,2))
