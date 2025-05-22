# ch01
def number():
    """
    n = int(input("type a number: ")).
    print(n ** 2).
    :param n: int.
    :print: nの2乗の結果.
    """
number()

# ch02
x="mozi"
def word():
    """
    print(x).
    :param x: 文字.
    :文字を出力.
    """
word()

# ch03
def number(v, w, x, y=4, z=5):
    """
    return v+w+x+y+z.
    :param v: 数字.
    :param w: 数字.
    :param x: 数字.
    :param y: 数字.
    :param z: 数字.
    :return: float sum of v, w, x, y and z.
    """
result = number(1,2,3)
print(result)

# ch04
x=8
def number():
    """
    return x/2.
    :param x: 数字.
    :rerurn: xを2で割った商.
    """
y=number()
print(y)
def number_2():
    """
    return y*4.
    :param y:xを2で割った商を代入.
    :return: yに4を掛けた積.
    """
print(number_2())

# ch05
def number():
    try:
        """
        n=input("type a number:").
        n=float(n).
        print(n).
        :param n:float.
        :print: nを出力.
        """
    except(ValueError):
        """
        print("Invalid input.").
        :print: エラー内容を出力.
        """

number()

