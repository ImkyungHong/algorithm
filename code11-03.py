import random
##함수(이 함수는 그대로 기억하면 도움됨)
def selectionSort(ary):
    n = len(ary)    #데이터의 개수
    for i in range(0, n-1):     #4개데이터 -> 사이클3번(n-1)
        minIndex = i 
        for k in range(i+1, n):  #제일 작은값 다음부터 도니까i+1
            if ary[minIndex] > ary[k]:
                minIndex = k 
        ary[i], ary[minIndex] = ary[minIndex], ary[i]
    return ary

##전역
dataAry = [random.randint(33,190) for _ in range(20)]


##메인
print('정렬 전 ->', dataAry)
dataAry = selectionSort(dataAry)

print('정렬 후 ->', dataAry)