while True:
    # 入力
    n, m = map(int, input().split())
    if n + m == 0:
        break
    a = list(map(int, input().split()))

    # 仮に答えを-1とする
    ans = -1
    # 答えを求める
    for i in range(n):
        for j in range(n):
            # 探索範囲を i < j とする
            if i >= j:
                continue
            # i番目とj番目を買うことにする
            price = a[i] + a[j]
            # 決まった金額を超えない場合
            if price <= m:
                # priceのほうが大きければそれに書き換え
                ans = max(ans, price)

    # ansが-1のとき、どの値も書き変わってない = 予算オーバー
    # そうでなければ、最大値を出力
    print("NONE" if ans == -1 else ans)
