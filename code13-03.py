##함수
def binarySearch(ary, fdata) :  #fdata:찾고자하는데이터
    pos = -1    # -1번쨰 위치는 없으니까 이걸로 return.못찾았당
    start = 0
    end = len(ary) -1
    while (start <= end):
        mid = (start + end) // 2
        if fdata == ary[mid]:
            return mid
        elif fdata > ary[mid]:
            start = mid +1  #오른쪽으로 
        else:
            end = mid -1    #왼쪽으로 
    return pos


##전역
dataAry = [50, 60, 105, 120, 150, 160, 162, 168, 177, 188]
findData = 162 #할머니키 


##메인
print('배열-->', dataAry)
position = binarySearch(dataAry, findData)
if position == -1:      #결과가 -1이면 못찾은 것 
    print('못찾음...')
else:
    print(findData, '는(은)', position, '위치에 있음')