def egcd(a,b):
    if(a<b):
        a, b = b, a
    if(b==0):
        return a,0,1

    g,t1,s1 = egcd(b, a%b)
    t = s1 - a//b * t1 
    s = t1

    return g,t,s



print(egcd(192,35))