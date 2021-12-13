with open('input.txt','r') as f:
    s = f.read()

s = s.strip('\n')
s = s.split('\n')

s = [int(x) for x in s] # we store the numbers in a array

ans = 0 # declaring our answer
for i in range(1,len(s)): # iterating from 1 index instead of 0
    ans+= int(s[i]>s[i-1]) # comparing and adding it in the answer

print(ans)
