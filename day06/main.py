with open('input.txt','r') as f:
    s = f.read().strip('\n')

a = list(map(int, s.split(",")))
b = [0]*9 # it will store the number if fish with particular timer

for x in a: b[x]+=1

d = 0
while d<256: # 80 or 256
    b1 = [0]*9
    b1[8] = b[0] # zero will add those 8's
    b1[6] = b[0] # also zero will go to 6
    for i in range(1,9): # otherwise from 1 to 8,
        b1[i-1]+=b[i] # they all will contribute to one on left

    b = b1[:]
    d+=1 # counting days

print(sum(b)) # total fishes
