#encoding = utf-8
__author__ = 'lg'

with open('H:\Programming\Python_Workspace\in.txt','r') as f:
    list1 = f.readline().split()
    list2 = f.readline().split()
    print(list1)
    print(list2)

#两个list的交集(法一) 时间复杂度为O(n^2)
def intersect(a,b):
    listRes = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                if a[i] not in listRes:
                    listRes.append(a[i])
    listRes.sort()
    print(listRes)

#两个list的交集（法二）　　时间复杂度为O(n^2)
def intersect_1(a,b):
    listRes = []
    for i in range(len(a)):
        if a[i] in b:
            if a[i] not in listRes:
                listRes.append(a[i])
    print(sorted(listRes))

#两个list的差集
def minus(a,b):
    listRes = []
    for i in range(len(a)):
        if a[i] not in b:
            listRes.append(a[i])
    print(sorted(listRes))

# list1 intersect list2
intersect(list1,list2)

# list1 minus list2
minus(list1,list2)

# list2 minus list1
minus(list2,list1)

