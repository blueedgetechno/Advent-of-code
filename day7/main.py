with open('input.txt','r') as f:
    s = f.read().strip('\n')

# s = "16,1,2,0,4,2,7,1,2,14"

a = list(map(int, s.split(",")))
i = 0 # left and right range for binary search
j = max(a)
d = dict()

def sumN(n):
    # return n            -> for part 1
    return (n*(n+1))//2 # -> for part 2

def fuel(m): # method to determine fuel
    if d.get(m,-1)!=-1: return d[m]

    c = 0
    for x in a:
        c+=sumN(abs(m-x))

    d[m] = c
    return c

def check(m): # checking the slope around a particular position
    c0 = fuel(m-1)
    c = fuel(m)
    c2 = fuel(m+1)

    if c0<=c<=c2: return 1 # returns 1 for positive slope
    if c0>=c>=c2: return -1 # and negative for negative slope
    else: return 0 # zero should be minima

while i<j:
    m = (i+j)//2
    f = check(m) # checks for slope
    if f==1: # if slope is greater than one
        j = m-1 # we have outrunned the minima, rollback
    elif f==-1: # otherwise we have yet to go for minima
        i = m+1 # so slide the left range to current m
    else:
        j = m # woala we found one
        break

print(j,fuel(j))
