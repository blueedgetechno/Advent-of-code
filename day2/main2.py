with open('input.txt','r') as f:
    s = f.read()

s = s.strip('\n')
s = s.split('\n')

s = [x.split() for x in s] # splitting each instruction in format of ["instruction", unit]

x = 0 # horizontal distance placeholder
y = 0 # vertical distance placeholder
aim = 0
for k in s:
    z = int(k[1])
    if k[0]=="forward":
        x+=z
        y+=aim*z
    elif k[0]=="down": aim+=z # aim getting increase on going down
    else: aim-=z # aim getting decrease on going up

print(x*y)
