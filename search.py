def search(list,item):
    n = len(list)
    for i in range(n):
        if list[i] == item:
            print(i+1)
            break;
        else:
            continue
list = [1,2,3,4,5]
search(list,3)

def sequentialSearch(alist,item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1

    return found

testlist = [1,2,32,8,17,19,42,13,0]
print(sequentialSearch(testlist,3))
print(sequentialSearch(testlist,13))
