# list=["苹果","香蕉","西瓜"]
# for i in list:
#     print(i)
# dict={"语文":88,"数学":66}
# for y in dict:
#     print(y,dict[y])
student=[
    {"name":'小明',"age":18,"score":88},
    {"name":'小红',"age":19,"score":92},
    {"name":'小刚',"age":20,"score":75}
]
for stu in student:
    print(f"{stu['name']}的成绩是{stu['score']}分,年龄是{stu['age']}")