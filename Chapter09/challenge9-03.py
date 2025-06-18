movies=[
        ["Top Gun","Risky Business","Minority Report"],
        ["Titanic","The Revenant","Inception"],
        ["Training Day","Man on Fire","Flight"]
        ]

import csv 

with open("movies.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    for i in movies:
        w.writerow(i)
