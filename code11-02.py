import random
## 함수 선언부
def findMinIndex(ary) :
    minIndex = 0
    for i in range(1, len(ary)) :
        if ( ary[minIndex] > ary [i]) :
            minIndex = i
    return minIndex


## 전역변수 
before = [random.randint(33,190) for _ in range(20)]
after = []


## 메인 코드
print('정렬 전 ->', before)

# before의 개수만큼 반복
# 가장 작은 위치를 알아내기
# 가장 작은 값을 after에 넣은 후, before에서는 지우기 

for _ in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])
    

print('정렬 후 ->', after)