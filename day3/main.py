with open('input.txt','r') as f:
    s = f.read()

s = s.strip('\n')
s = s.split('\n')

a = [0]*len(s[0])

for x in s:
    for i,y in enumerate(x):
        a[i]+= 2*int(y)-1 # adding 1 for 1 and -1 for 0

gr = 0 # gamma rate
er = 0 # epsilon rate
for i,x in enumerate(a): # making the binary number
    gr*=2
    er*=2
    if x>0: gr+=1 # appending one after gamma rate when 1 is more often
    else: er+=1 # otherwise epsilon rate is gonna get that 1

print(gr*er)
