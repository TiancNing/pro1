mainui = """
**************************
商店
**************************
按 1 购买
按 2 结算
按 q 退出
**************************
"""
product_info={101:{'name':'倚天剑','price':10000},
              102:{'name':'屠龙刀','price':50000},
              103:{'name':'八宝粥','price':42100}}

cart=[]
def main():
   while True:
       print(mainui.strip())
       selet=input()
       if selet.lower()=='q':
           break
       elif selet=='1':
           point_info()
           gotocart()
       elif selet=='2':
           order_print()
           pay(cal_sumMon())
       else:
           pass
def point_info():
    print('*'*35)
    print('编号'.center(10)+'商品名'.center(10)+'价格'.center(10))
    for k in product_info.keys():
        print(str(k).center(10)+product_info[k]['name'].center(10)+str(product_info[k]['price']).center(10))
    print('*'*35)
def gotocart():
    while True:
        id=int(input('请输入商品编号'))

        if id not in product_info:
            print("你选择的商品不存在，请重新选择")
            continue
        num = int(input('请输入商品数量'))
        jud=0
        for sp in cart:
            for k in sp.keys():
                if k==id:
                    jud=1
        if jud==0:
            cart_dict={id:{'name':product_info[id]['name'],'unitprice':product_info[id]['price'],'count':num,'price':product_info[id]['price']*num}}
            cart.append(cart_dict)
        else:
            for sp in cart:
                for k in sp.keys():
                    if k == id:
                        sp[id]['count']=sp[id]['count']+num
                        sp[id]['price']=sp[id]['unitprice']*sp[id]['count']
        print('添加购物车成功,是否继续:(Y/N)')
        jud=input()
        if jud.upper()=='N':
            break
def order_print():
    print('*'*50)
    print('购物车')
    print('*'*50)
    print('%-8s %-8s %-8s %-8s %-8s'%('编号','商品名','单价','数量','总价'))
    for order in cart:
        for k,v in order.items():
            print('%-9d %-9s %-9d %-9d %-9d' % (k, v['name'], v['unitprice'], v['count'], v['price']))
    print('*' * 50)
def cal_sumMon():
    sum=0
    for order in cart:
        for v in order.values():
            sum+=v['price']
    return sum
def pay(sum):
    print('共{0}件商品，总金额为{1}元,请输入金额'.format(len(cart),sum))
    while True:
        jin = int(input())
        if jin<sum:
            print('金额不足，请重新输入')
            continue
        else:
            print('应收{0}元,实收{1}元,找零{2}元'.format(sum,jin,jin-sum))
            cart.clear()
            break


if __name__ == '__main__':
    main()
