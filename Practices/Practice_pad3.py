# bar = {}

# bar["father"] = "mother"
# print(bar["father"])

# bar = {"mother" : 10, "father" : 20, "boy" : 30, "girl" : 40, "man" : 50, "lady" : 60}

# for key in bar.keys(): # 17번과 같은 기능이다.
#     print(key)
    
# for value in bar.values():
#     print(value)

# for key, value in bar.items():
#     print(key, value)
    
# for key in bar: # 8번과 같은 기능이다.
#     print(key)
    
# bar = {"1st_user" : {"name" : "조원준", "age" : 24, "brith" : 6.6}, "2nd_user" : {"name" : "김성식", "age" : 24, "birth" : 1.14}}

# print(bar["1st_user"])
# print(bar["1st_user"]["name"])
# print(bar["1st_user"]["age"])
# print(bar["1st_user"]["brith"])
# print(bar["2nd_user"])
# print(bar["2nd_user"]["name"])
# print(bar["2nd_user"]["age"])
# print(bar["2nd_user"]["birth"])

# bar = {"mother" : 10, "father" : 20, "boy" : 30, "girl" : 40}

# bar['man'] = "50"
# bar['lady'] = "60"
# print(bar)

# bar['man'] = "100"
# print(bar)

# if "father" in bar:
#     print("True")
# else:
#     print("False")

# del bar["boy"]
# print(bar)

# if "boy" in bar:
#     print("True")
# else:
#     print("False")

# if "mother" in bar.keys():
#     print("Yes")
# else:
#     print("No")
    
# if 20 in bar.values():
#     print("yes!")
# else:
#     print("No...")

std_grades = {}

std_grades[240001] = ["이영일", 10, 20, 30, 60, 30]
std_grades[240002] = ["이영이", 100, 200, 300, 600, 300]
std_grades[240003] = ["이영삼", 1000, 2000, 3000, 6000, 3000]
std_grades[240004] = ["이영사", {"국어" : 100, "수학" : 70, "영어": 80}]

print(sum(std_grades[240004][1].values()))
print(format(sum(std_grades[240004][1].values()) / len(std_grades[240004][1]),".2f"))

