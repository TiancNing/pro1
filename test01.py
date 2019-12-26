# grade=int(input("请输入成绩"))
# if grade>90 and grade<=100:
#     print("优秀")
# elif grade>80 and grade<=90:
#     print("良好")
# elif grade>70 and grade<=80:
#     print("中等")
# elif grade>=60 and grade<=70:
#     print('及格')
# elif grade<60 and grade>=0:
#     print("不及格")
# else:
#     print("输入错误")
# print(help(range))
money=100000
for i in range(3):
    password = int(input("请输入密码"))
    if(password==123456):
        print("密码正确，欢迎进入本系统")
        while True:
            print("""
    请选择功能：
    1.查询
    2.取款
    0.离开
            """
            )
            selet=int(input())
            if selet==0:
                break
            elif selet==1:
                print("余额为:",money,sep='')
            elif selet==2:
                while True:
                    print("""
    请输入取款金额,输入 0 以结束取款。
                    """
                    )

                    jud=True
                    getMon=int(input())
                    if getMon<=money and getMon>0:
                        money=money-getMon
                        print("成功取出",getMon,"元，","剩余金额为：",money,sep='')
                    elif getMon>money:
                        while True:
                            print("""
    取款金额超出余额，请选择操作：
    1.继续输入
    2.退出取款
                                  """
                                  )
                            cel = int(input())
                            if cel == 1:
                                continue
                            elif cel ==2:
                                jud=False
                                break
                    elif getMon==0:
                        break
                    else:print("取款金额格式不正确")
                    if jud==False:
                        break
            else:
                print("指令错误，请重新输入")
        else:print("退出成功")

        break
    print("密码错误")
else:
    print("输入次数已达上线，今日不可登录！")



