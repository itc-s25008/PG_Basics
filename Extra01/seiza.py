

try:
    seiza = ["","水瓶","魚","牡羊","牡牛","双子","蟹","獅子","乙女","天秤","蠍","射手","山羊"]
    tuki = int(input("月を入力"))
    hi = int(input("日を入力"))
    if tuki ==1:
        if hi >= 1 and hi < 21:
            print("あなたの星座は" + seiza[12] + "座です")
        elif hi >=21 and hi <= 31:
            print("あなたの星座は" + seiza[tuki] + "座です")
    elif tuki ==2:
        if hi >= 1 and hi < 20:
            print("あなたの星座は" + seiza[tuki-1] + "座です")
        elif hi >=20 and hi <= 29:
            print("あなたの星座は" + seiza[tuki] + "座です")
    elif tuki ==3:
        if hi >= 1 and hi < 22:
            print("あなたの星座は" + seiza[tuki-1] + "座です")
        elif hi >=22 and hi < 31:
            print("あなたの星座は" + seiza[tuki] + "座です")
    elif tuki ==4:
        if hi >= 1 and hi < 21:
            print("あなたの星座は" + seiza[tuki-1] + "座です")
        elif hi >=21 and hi <= 30:
            print("あなたの星座は" + seiza[tuki] + "座です")
    elif tuki ==5:
        if hi >= 1 and hi < 22:
            print("あなたの星座は" + seiza[tuki-1] + "座です")
        elif hi >=22 and hi <= 31:
            print("あなたの星座は" + seiza[tuki] + "座です")
    elif tuki ==6:
        if hi >= 1 and hi < 23:
            print("あなたの星座は" + seiza[tuki-1] + "座です")
        elif hi >=23 and hi <= 30:
            print("あなたの星座は" + seiza[tuki] + "座です")
    elif tuki ==7:
        if hi >= 1 and hi < 24:
            print("あなたの星座は" + seiza[tuki-1] + "座です")
        elif hi >=24 and hi <= 31:
            print("あなたの星座は" + seiza[tuki] + "座です")
    elif tuki ==8:
        if hi >= 1 and hi < 24:
            print("あなたの星座は" + seiza[tuki-1] + "座です")
        elif hi >=24 and hi <= 31:
            print("あなたの星座は" + seiza[tuki] + "座です")
    elif tuki ==9:
        if hi >= 1 and hi < 24:
            print("あなたの星座は" + seiza[tuki-1] + "座です")
        elif hi >=24 and hi <= 30:
            print("あなたの星座は" + seiza[tuki] + "座です")
    elif tuki ==10:
        if hi >= 1 and hi < 25:
            print("あなたの星座は" + seiza[tuki-1] + "座です")
        elif hi >=25 and hi <= 31:
            print("あなたの星座は" + seiza[tuki] + "座です")
    elif tuki ==11:
        if hi >= 1 and hi < 24:
            print("あなたの星座は" + seiza[tuki-1] + "座です")
        elif hi >=24 and hi <= 30:
            print("あなたの星座は" + seiza[tuki] + "座です")
    elif tuki ==12:
        if hi >= 1 and hi < 23:
            print("あなたの星座は" + seiza[tuki-1] + "座です")
        elif hi >=23 and hi <= 31:
            print("あなたの星座は" + seiza[tuki] + "座です")
    else:
        print("数字のみ入力してください")
except ValueError:
    print("数字のみ入力してください")
