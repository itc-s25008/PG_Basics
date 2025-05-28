features = {"身長": "180", "好きな色": "水色", "好きな作家":"知念実希人"}

n = input("キーを入力してください:")
if n in features:
    features = features[n]
    print(features)
else:
    print("見つかりません。")
