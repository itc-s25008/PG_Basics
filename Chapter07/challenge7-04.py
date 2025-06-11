number=[2,3,5,7,]
while True:
    print("Type q to quit")
    a=input()
    try:
        if a =="q":
            break
        else:
            a=int(a)
    except ValueError:
        print("「数字を入力するか、qで終了します」")
        continue
    if a in number:
        print("正解")
    else:
        print("不正解")
