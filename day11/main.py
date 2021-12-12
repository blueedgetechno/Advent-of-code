with open('input.txt','r') as f:
    s = f.read().strip('\n')

s = s.split("\n")
a = []

for x in s:
    a+=[],
    for y in x: a[-1]+=int(y),

n = len(a)
m = len(a[0])
ans1 = [0]

def isValid(i,j):
    return 0<=i<n and 0<=j<m

def bright():
    for i in range(n):
        for j in range(m):
            a[i][j]+=1

def flash(i,j):
    ans1[0]+=1
    a[i][j] = 0
    for dx in range(-1,2):
        for dy in range(-1,2):
            if (dx!=0 or dy!=0) and isValid(i+dx,j+dy):
                if a[i+dx][j+dy]!=0:
                    a[i+dx][j+dy]+=1
                    if a[i+dx][j+dy]>9:
                        flash(i+dx,j+dy)

def go():
    c = 1
    z = 0
    while c!=0:
        # print("ok")
        c = 0
        z = 0
        for i in range(n):
            for j in range(m):
                if a[i][j]>9:
                    c+=1
                    flash(i,j)
                else:
                    if a[i][j]==0:
                        z+=1

    return z==n*m

d = 0
while d>=0:
    bright()
    if go():
        print(d+1) # ans2
        break
        # exit()
    d+=1

# print(ans1[0])
