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

# rectifying data completed

# marking function
def mark(i,a): # receives index of board and number to be marked
    for j in range(5):
        for k in range(5):
            if b[i][j][k]==a: # iterates and check
                b[i][j][k]=-1 # sets -1 at that place
                break

def check(i):
    rw = [0,0,0,0,0]
    cl = [0,0,0,0,0]
    for j in range(5):
        for k in range(5):
            rw[j]+=b[i][j][k] # sums the rows
            cl[k]+=b[i][j][k] # as well as columns

    for x in rw:
        if x==-5: return True # choosing -1 at place helps

    for x in cl:
        if x==-5: return True # because only five -1 can make -5

    return False

def sumMat(i): # speaks for itself
    sm = 0
    for j in range(5):
        for k in range(5):
            if b[i][j][k]!=-1:
                sm+=b[i][j][k]

    return sm

bl = len(b)
ans = 0
for a in q:
    for i in range(bl):
        mark(i,a) # marking the number on each board
        if check(i): # checking for win
            sm = sumMat(i) # summing up
            ans = a*sm
            print(ans) # printing the answer
            exit() # exiting
