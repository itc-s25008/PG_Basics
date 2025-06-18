movies=[
        ["トップガン","卒業白書","マイノリティ・リポート"],
        ["タイタニック","レヴェナント","インセプション"],
        ["トレーニング デイ","マイ・ボディガード","フライト"]
        ]

import csv

with open("movies2.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    for i in movies:
        w.writerow(i)
