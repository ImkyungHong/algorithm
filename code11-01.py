def findMinIndex(ary): 
    minINdex = 0
    for i in range(1, len(ary)):
        if (ary[minIndex] > ary[i]):
            minIndex = i 

    return minIndex



testAry = [55, 88, 33, 77]
minPos = findMinIndex(testAry)
print('최소값-->', testAry[minPos])
