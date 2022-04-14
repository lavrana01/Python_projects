N = 2
p1 = [14,15,16]

p2 = [14,15,16]

p3 = [12,13,14]

if N>=1 & N<=25:
    def fac():
        c1 = min(p1)
        a = p1.index(c1)
        del p2[a]
        print(p2)
        c2 = min(p2)
        b = p2.index(c2)
        del p3[a]
        del p3[b]
        c3 = min(p3)
        c = c1 + c2 + c3
        print("Minimum cost for world tour is:",c)

fac()


        

