'''
def avg(a,b):
    c=a+b
    print(c)



a=23
b=34
avg(a,b)

def name(p):
    gr="hello "+p
    print(gr)

q="Nish"
name(q)
'''


def rec(n):
    if( n==0 | n==1):
        return 1
    else:
       return n*rec(n-1)


t=rec(5)
print(t)