## 함수 
def openBox():
    global count
    print('상자열기')
    count -= 1  # 10 9 8 7 6 하나씩 줄어들어
    if count == 0:
        print('**선물 넣기 **')
        return
    openBox()
    print('상자닫기')

## 전역
count = 5

##메인
openBox()     

