# 最大公約数を、ユークリッドの互除法により求める
def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


while True:
    # 入力
    a, b, c, d = map(int, input().split())

    # もしすべての要素が0であれば終了
    if a + b + c + d == 0:
        break

    # すべての数の最大公約数を求める
    g = a
    g = gcd(g, b)
    g = gcd(g, c)
    g = gcd(g, d)

    # 答えはすべての数の最大公約数 g
    print(g)
