# dict1={'姓名':'tcn','age':12,'score':[78,85,89]}
# dict2={'姓名':'tcn1','age':16,'score':[78,85,89],'tall':175}
# print(dict1)
#
# dict1.update(dict2)
# dict1.pop('tall')
# print(dict1['姓名'])
# for k,v in dict1.items():
#     print(k,v)
#
# mdict={i:i**2 for i in range(10) if i%2==0}
# print(mdict)
# s=set()
# s1={1,2,3,4,7,6,8}
# s2={2,3,7,8}
# print(s1>s2)
# s3=s1 & s2
# print(s3)
# s4=s1|s2
# print(s4)
# s5=s1-s2
# print(s5)
# s6=s1^s2
# print(s6)
def sort1(a,b,c):
    print('a=',a,',b=',b,'c=',c)
    l=[a,b,c]
    l.sort(reverse=True)
    for i in l:
        print(i)
def sayby():
    return 'dasd'

def sayHi(name):
    print('你好',name)
def sayHello():
    print("hello")
def myrange(num):
    l=[]
    i=0
    while i<num:
       l.append(i)
       i+=1
    return l

if __name__ == '__main__':
    print(myrange(5))
    sayHello()
    sayHi(22)
    print(sayby())
    sort1(*[532,54,78])



