with open('input.txt','r') as f:
    s = f.read()

s = s.strip('\n')
s = s.split('\n')

s = [x.split() for x in s] # splitting each instruction in format of ["instruction", unit]

x = 0 # horizontal distance placeholder
y = 0 # vertical distance placeholder
for k in s:
    z = int(k[1])
    if k[0]=="forward": x+=z
    elif k[0]=="down": y+=z # depth increases on going down
    else: y-=z # depth decreases on going up

print(x*y)
