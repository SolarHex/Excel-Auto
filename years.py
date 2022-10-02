


dic = {
    "Winter":{
        "January":1,
        "February":2,
    },
    "Spring":{
        "March":3,
        "April":4,
        "May":5
    },
    "Summer":{
        "June":6,
        "July":7,
        "August":8
    },
    "Autumn":{
        "September":9,
        "October":10,
        "November":11,
        "December":12
    }
}

for i in dic:
    number = input("Number of month...")
    if dic[i]["Winter"] == number:
        print(dic[i]["January"])
    else:
        print("NO")
