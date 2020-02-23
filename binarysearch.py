##递归方法
def binarySearch(list,item):
    found = True
    middle = (0+len(list)-1)//2
    middleitem = list[middle]
    if item == middleitem:
        found = True
        return found
        
    else:
        if item < middleitem:
            binarySearch(list[:middle+1],item)
        else:
            binarySearch(list[middle:],item)
 

a = [1,2,3,4,5,6,7]
print(binarySearch(a,3))


#非递归方法
def binarySearch(list,item):
    first = 0
    last = len(a)-1
    found = False
    while first < last and not found:
        middleitem = list[(first+last)//2]
        if item == middleitem:
            found = True
        else:
            if item < middleitem:
                last = middleitem
                found = False
            else:
                first = middleitem
                found = False
    return found
          
        
a = [1,2,3,4,5,6,7]
print(binarySearch(a,3))



                
