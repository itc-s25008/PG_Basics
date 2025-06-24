import random

# 1...グー 2...チョキ 3...パーとする

while True:

    try:
        x = int(input("1グー 2チョキ 3パー:"))

        r = random.randint(1,3)
        janken = ["", "グー", "チョキ","パー"]

        if x == r:
            print("あなた:" + janken[x] + "  コンピュータ:" + janken[r])
            print("あいこ")
        elif x == 1:
            if r == 2:
                print("あなた:" + janken[x] + "  コンピュータ:" + janken[r])
                print("あなたの勝ちです")
            else:
                print("あなた:" + janken[x] + "  コンピュータ:" + janken[r])
                print("あなたの負けです")
        elif x == 2:
            if r == 3:
                print("あなた:" + janken[x] + "  コンピュータ:" + janken[r])
                print("あなたの勝ちです")
            else:
                print("あなた:" + janken[x] + "  コンピュータ:" + janken[r])
                print("あなたの負けです")
        elif x == 3:
            if r == 1:
                print("あなた:" + janken[x] + "  コンピュータ:" + janken[r])
                print("あなたの勝ちです")
            else:
                print("あなた:" + janken[x] + "  コンピュータ:" + janken[r])
                print("あなたの負けです")
        else:
            break
    except ValueError:
        break
