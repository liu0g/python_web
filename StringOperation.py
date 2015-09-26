#encoding = utf-8
__author__ = 'lg'

list1 = ['java','python','ruby','perl','mac']
list2 = ['linux','mac','windows','ruby']

#两个list的交集(法一) 时间复杂度为O(n^2)
def intersect(a,b):
    listRes = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                if a[i] not in listRes:
                    listRes.append(a[i])
    return listRes

#两个list的交集（法二）　　时间复杂度为O(n)
def intersect_1(a,b):
    listRes = []
    for i in range(len(a)):
        if a[i] in b:
            if a[i] not in listRes:
                listRes.append(a[i])
    return listRes

#两个list的差集
def minus(a,b):
    listRes = []
    for i in range(len(a)):
        if a[i] not in b:
            listRes.append(a[i])
    return listRes

# 按字母表输出字符串
def alphabet_output(listPram):
    sortedList = []
    for i in range(len(listPram)):
        sortedStrRes = ''
        sortedStrList = sorted(listPram[i])
        for j in range(len(sortedStrList)):
            sortedStrRes += sortedStrList[j]
        sortedList.append(sortedStrRes)
    print(sortedList)

# list1 intersect list2
intersectList = intersect_1(list1,list2)
alphabet_output(intersectList)

# list1 minus list2
minusList = minus(list1,list2)
alphabet_output(minusList)

# list2 minus list1
minusList_1 = minus(list2,list1)
alphabet_output(minusList_1)
