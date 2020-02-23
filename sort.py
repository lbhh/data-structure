##bubbleSort冒泡排序
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
            
#shortBubbleSort冒泡排序改进
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum>0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum-1

alist = [20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)

##selectionSort选择排序
def selecitionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


##insertionSort插入排序
def insertionSort(alist):
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1
        alist[position] = currentvalue

##shellsort谢尔排序
def shellSort(alist):
    sublistcount = len(alist)//2 ##间隔设定
    while sublistcount > 0:

        for startposition in range(sublistcount):  #子列表排序
            gapInsertionSort(alist,startposition,sublistcount)

        print("After increments of size",sublistcount,"The list is",alist)

        sublistcount = sublistcount//2  #间隔缩小

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position-gap

        alist[position]=currentvalue
