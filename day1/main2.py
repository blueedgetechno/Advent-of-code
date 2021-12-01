with open('input.txt','r') as f:
    s = f.read()

s = s.strip('\n')
s = s.split('\n')

s = [int(x) for x in s]

ans = 0
for i in range(3,len(s)):
    ans+= int(s[i]>s[i-3])

print(ans)
