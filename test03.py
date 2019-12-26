
def square(h,w,c='*'):
    for i in range(h):
        for j in range(w):
            print(c,end='')
        print()
def myrange(*args):
    start=0
    end=0;
    jump=1
    if len(args)==1:
        end=args[0]
    elif len(args)==2:
        start=args[0]
        end=args[1]
    elif len(args)==3:
        start = args[0]
        end = args[1]
        jump=args[2]
    elif len(args)==0:
        pass
    else:
        print("输入有误")

    l=[]
    if jump<0:
        i=start
        while i>end:
            l.append(i)
            i+=jump
    else:
        i = start
        while i<end:
            l.append(i)
            i+=jump
    return l
def fun2(*args,p,w):
    print(args)
    print(p)
    print(w)
def fun3(*,name,pwd):
    print(name,pwd)
def fun4(**kwargs):
    print(kwargs)
def fun5(a,b,c=1,*args,name,age,sex='男',**kwargs):
    print('a',a)
    print('b',b)
    print('c',c)
    print('args',args)
    print('name',name)
    print('age',age)
    print('sex',sex)
    print('kwargs',kwargs)
if __name__ == '__main__':
    s=[{101:{'pricee':10}}]
    for a in s:
        for k,v in a.items():
            if k==101:
                a[101]['price']=2
                print(a)
    print(s)
    #fun5(1,2,3,4,5,6,7,8,name='tcn',age='14',ll='d',zz='d')
    #fun4(name='tcn',age=17)
   # fun3(name='dsa',pwd='das')
    #fun2(1,2,3,1,2,p=45,w=45)
    #for i in myrange(7,1,-1):
     #   print(i,end=' ')
    # square(4,5,'♥')
    # fun2(4,25,'das','das')
