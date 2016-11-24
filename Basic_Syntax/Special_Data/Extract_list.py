__auth__ = 'NguyenTTin'


fruits = ['Juice', 'Tomato', 'Potatoes', 'Banana', 'Tomato', 'Banana']
result = []
for i in fruits:
    result.append(fruits.count(i))
result=list(zip(fruits,result))
print(result)
for i in result:
    if result.count(i)>1:
        result.remove(i)

print(result)

# fruits = ['Juice', 'Tomato', 'Potatoes', 'Banana', 'Tomato', 'Banana']
#
# uniqueList = []
# for fruit in fruits:
#     if uniqueList.count(fruit) == 0:
#         uniqueList.append(fruit)
#
# print(uniqueList)
#
# def getUniqueList(inList: list) -> list:
#     uniqueList = []
#     for item in inList:
#         if uniqueList.count(item) == 0:
#             uniqueList.append(item)
#
#     return uniqueList
#
# print(getUniqueList(fruits))
#
#
# def filterDup(list):
#     for item in list:
#         while list.count(item) > 1:
#             list.remove(item)         #also use: del list[list.index(item)]
#     return list
#
# print(filterDup(["tom", "jerry", "dog", "tom"]))