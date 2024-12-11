#tc:0 (n)
#sc:0(1)

def fun(n):
    pOne=1
    PTow=1
    for i in range(2,n+1):
        current=pOne+PTow
        pOne=PTow
        PTow=current
    return current
n=5
print(fun(n))