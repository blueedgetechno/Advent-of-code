with open('input.txt','r') as f:
    s = f.read().strip('\n')

s = s.split("\n")
a = [x.split("-") for x in s]

class graph:
    def __init__(self,gr=None):
        if gr==None:
            gr={}
        self.gr = gr
        self.path = 0

    def vertices(self):
        return list(self.gr.keys())

    def edges(self):
        edgename = []
        for vrtx in self.gr:
            for nxtvrtx in self.gr[vrtx]:
                if (nxtvrtx, vrtx) not in edgename and (nxtvrtx, vrtx)[::-1] not in edgename:
                    edgename.append((vrtx, nxtvrtx))
        return edgename

    def addVertex(self,v):
        self.gr[v]=self.gr.get(v,[])

    def removeVertex(self, v):
        for x in self.gr[v]:
            self.gr[x].remove(v)

        self.gr.pop(v)

    def addEdge(self,v1,v2):
        self.gr[v1]=self.gr.get(v1,[])
        self.gr[v2]=self.gr.get(v2,[])
        if v2 not in self.gr[v1]:
            self.gr[v1].append(v2)
        if v1 not in self.gr[v2]:
            self.gr[v2].append(v1)

    def search(self,v,pt="",st=""):
        if v=="end":
            self.path+=1
            return

        pt+=v+"-"

        for x in self.gr[v]:
            if x.islower():
                if (x+"-") not in pt:
                    self.search(x,pt,st)
                elif st=="":
                    self.search(x,pt,x)

            elif x.isupper():
                self.search(x,pt,st)

st = []
b = []
for x in a:
    if "start" in x:
        if x[0]=="start": st+=x[1],
        else: st+=x[0],
    else:
        b+=x,

g = graph()
for x in st:
    g.addVertex(x)

for x in b:
    g.addEdge(x[0],x[1])

for x in st:
    g.search(x)

print(g.path)
