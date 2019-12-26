
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
def fun2(*args):

    print(args)
if __name__ == '__main__':
    for i in myrange(7,1,-1):
        print(i,end=' ')
    # square(4,5,'♥')
    # fun2(4,25,'das','das')
