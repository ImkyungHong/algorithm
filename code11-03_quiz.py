## 선택 정렬하라 
import random
def selectionSort(ary):
    n = len(ary)    #데이터의 개수
    for i in range(0, n-1):     #4개데이터 -> 사이클3번(n-1)
        maxIndex = i 
        for k in range(i+1, n):  #제일 작은값 다음부터 도니까i+1
            if ary[maxIndex] < ary[k]:
                maxIndex = k 
        ary[i], ary[maxIndex] = ary[maxIndex], ary[i]
    return ary


## -100부터 100까지 숫자를 랜덤하게 30개 만들기 
dataAry = [random.randint(-100, 100) for _ in range(30)]

## 내림 차순으로 정렬하기
print('정렬 전 ->', dataAry)

dataAry = selectionSort(dataAry)
print('정렬 후 ->', dataAry)