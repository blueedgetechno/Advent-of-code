with open('input.txt','r') as f:
    s = f.read()

s = s.strip('\n')
s = s.split('\n')

s = [int(x) for x in s]

ans = 0
for i in range(3,len(s)):
    # we can say the prev and this sums will share two elements in common
    # so we can just compare this element with 3rd previous one
    # 0 A
    # 1 A B -- ignoring these as they
    # 2 A B -- are common in both sums
    # 3   B
    ans+= int(s[i]>s[i-3])

print(ans)
