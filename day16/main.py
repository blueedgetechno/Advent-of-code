with open('input.txt', 'r') as f: s = f.read().strip('\n')

a = ""
for x in s:
    b = bin(int(x,16))[2:]
    a += "0"*(4-len(b)) + b

ans = [0,0]
def solve(t,vals):
    val = vals[0]
    if t==0: val+=sum(vals[1:])
    if t==1:
        for x in vals[1:]: val*=x
    if t==2:
        for x in vals: val = min(val,x)
    if t==3:
        for x in vals: val = max(val,x)
    if t==5: val = 1 if val>vals[1] else 0
    if t==6: val = 1 if val<vals[1] else 0
    if t==7: val = 1 if val==vals[1] else 0
    return val

def find(i):
    v = int(a[i:i+3],2)
    ans[0]+=v
    t = int(a[i+3:i+6],2)
    ln = 6

    if t==4:
        j = i+6
        lv = "0"
        while True:
            lv+=a[j+1:j+5]
            j+=5
            ln+=5
            if a[j-5]=="0": break

        return [ln, int(lv,2)]

    else:
        id = int(a[i+6])^1
        ln+=1
        vals = []
        ln += 11 + id*4
        sp = int(a[i+7:i+ln],2)
        j = i+ln
        if id:
            ln+=sp
            while sp>0:
                spv = find(j)
                j+=spv[0]
                sp-=spv[0]
                vals+=spv[1],

        else:
            while sp>0:
                spv=find(j)
                j+=spv[0]
                ln+=spv[0]
                vals+=spv[1],
                sp-=1

        return [ln, solve(t,vals)]

ans[1] = find(0)[1]
print(ans[0]) # for part 1
print(ans[1]) # for part 2
